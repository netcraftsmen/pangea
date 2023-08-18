#!/opt/pangea/bin/python3

# Copyright: (c) 2023, BlueAlly NetCraftsmen, LLC
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: intel

short_description: Intel actions for Pangea

version_added: "1.0.0"

description:
  - This module provides functionality to invoke ....

requirements:
  - Python package pangea-sdk

options:
    token:
        description: Bearer token for authentication
        required: true
        type: str
        default: PANGEA_TOKEN environment variable
    domain:
        description: the cloud instance domain name, e.g. aws.us.pangea.cloud
        required: true
        type: str
        default: PANGEA_DOMAIN environment variable
    verbose:
        description: Echo the API parameters in the response
        required: false
        default: false
        type: bool
    raw:
        description: Include raw data from this provider
        required: false
        default: false
        type: bool
    action:
        description: Specifies the action to perform
        required: true
        choices: ['user', 'ip', 'url', 'domain']
        type: str
    user_intel:
        description:
          - Specify one of the following rguments for looking up breached users
        required: true
        choices: ['email', 'ip', 'username', 'phone_number']
        type: dict

author:
    - Joel W. King (@joelwking)
'''

EXAMPLES = r'''

    - name: User Intel email
      netcraftsmen.pangea.intel:
        token: '{{ token }}'
        domain: aws.us.pangea.cloud
        action: user
        parameters:
          email: "programmable.networks@gmail.com"
      register: pangea

    - name: User Intel IP
      netcraftsmen.pangea.intel:
        token: '{{ token }}'
        domain: '{{ domain }}'
        action: user
        parameters:
          ip: '192.0.2.1'
          raw: true
          verbose: true
          start: "2022-05-15"
          end: "2023-01-15"
      register: pangea

'''

RETURN = r'''

changed:
    description: did the module change the remote server
    type: bool
    returned: always
fail:
    description: for internal use, indicates if module.fail is to be called
    type: bool
    returned: always
msg:
    description: an error message or other information returned as to the status
    type: str
    returned: optional
    sample: "Status Code: ...."
data:
    description: data returned from the API call of the requested action
    type: dict
    returned: success
    sample: 'sample returned output'
'''


from ansible.module_utils.basic import AnsibleModule

import os

try:
    import pangea.exceptions as pe
    from pangea.config import PangeaConfig
    from pangea.services import UserIntel
    from pangea.services.intel import HashType
    from pangea.tools import logger_set_pangea_config
    from pangea.utils import get_prefix, hash_sha256
    HAS_PGA = True
except ImportError:
    HAS_PGA = False

def user_intel(params, intel):
    """ The User Intel service allows you to check a large repository of breach data to see if a user's 
        Personally Identifiable Data (PII) or credentials have been compromised.
    """
    parameters = params.get('parameters')

    try:
        response = intel.user_breached(**parameters)
    except pe.PangeaAPIException as e:
        return dict(fail=True, msg=f"User Intel Error: {e.response.summary} {e.errors}")
    
    return dict(data=response.json)

def main():
    """ Main logic flow
    """
    module = AnsibleModule(
        argument_spec=dict(
            token=dict(type='str', required=False, nolog=True, default=os.getenv("PANGEA_INTEL_TOKEN")),
            domain=dict(type='str', required=False, default=os.getenv("PANGEA_DOMAIN")),
            parameters=dict(type='dict', options=dict(
                email=dict(type='str', required=False, default=None),
                username=dict(type='str', required=False, default=None),
                phone_number=dict(type='str', required=False, default=None),
                ip=dict(type='str', required=False, default=None),
                provider=dict(type='str', required=False, default="spycloud"),
                start=dict(type='str', required=False),
                end=dict(type='str', required=False),
                verbose=dict(type='bool', required=False, default=False),
                raw=dict(type='bool', required=False, default=False),  
                )),
            action=dict(type='str', required=True, choices=['user', 'ip', 'url', 'domain'])
            ),
        supports_check_mode=False
    )

    # raise Exception(module.params)
    if not HAS_PGA:
        module.fail_json(msg="The Python SDK, pangea-sdk, is required!")

    # Create a case structure to call the appropriate action
    supported_actions = dict(user=user_intel)
                             # ip=ip_intel,
                             # url=url_intel,
                             # domain=domain_intel)

    # Get the function name associated with the action called by the user
    run_action = supported_actions.get(module.params.get('action'))

    # Run the function associated with the action, pass the module parameters and object
    config = PangeaConfig(domain=module.params.get("domain"))
    intel = UserIntel(module.params.get("token"), config=config, logger_name="intel")
    logger_set_pangea_config(logger_name=intel.logger.name)
    action_result = run_action(module.params, intel)

    if action_result.get('fail'):
        module.fail_json(msg=f"{action_result.get('msg')}")

    result = dict(changed=False, fail=False, msg='')    # Seed the result dictionary
    result.update(action_result)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
