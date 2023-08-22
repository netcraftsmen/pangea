# pangea
Pangea has a comprehensive security platform that you can leverage with simple API calls for authentication, audit logging, secrets management, sensitive data removal, and intelligence services.

## Pangea Securathon

ABOUT THE CHALLENGE: Health & Wealth Hackathon is a great opportunity to build your security skills using Pangea APIs for more details see <https://healthandwealth.devpost.com/>. The deadline is 18 September 2023.

## Ansible Collection

This repository contains an Ansible Collection with a module to interface with Pangea Cloud.

The `playbooks` directory contains two sample playbooks. Playbook `pb.intel_test.yml` is used to document the test cases. The playbook `pb.breach_user_check.yml` illustrates if a username, email or phone number has been exposed in a security breach. 

### Module Documentation

```
> NETCRAFTSMEN.PANGEA.INTEL    (/workspaces/pangea/collections/ansible_collections/netcraftsmen/pangea/plugins/modules/intel.py)

        This module provides User Intel functionality to determine if
        an email address, username, phone number, or IP address was
        exposed in a security breach. The Domain Intel service
        retrieves intelligence about known domain names, providing
        insight into the reputation of a domain. The URL Intel service
        retrieves intelligence about the reputation of a URL.

ADDED IN: version 1.0.0 of netcraftsmen.pangea

OPTIONS (= is mandatory):

= action
        Specifies the action to perform
        choices: [user, url, domain]
        type: str

= domain
        the cloud instance domain name, e.g. aws.us.pangea.cloud
        default: PANGEA_DOMAIN environment variable
        type: str

- logger
        enable interal logging, creates a file in current directory
        default: false
        type: str

= parameters
        Specify one or more parameters associated with an action.
        choices: [raw, verbose, provider, email, phone_number, username, ip, url, domain, start, end]
        type: dict

= token
        Bearer token for authentication
        default: PANGEA_TOKEN environment variable
        type: str


NOTES:
      * The phone number has a minLength 7, maxLength 15.
      * start and end are dates is the form of "2022-05-15"


REQUIREMENTS:  Python package pangea-sdk

AUTHOR: Joel W. King (@joelwking)

EXAMPLES:

- name: User Intel email
      netcraftsmen.pangea.intel:
        token: '{{ token }}'
        domain: aws.us.pangea.cloud
        action: user
        parameters:
          email: "bob@example.net"
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

    - name: Domain reputation
      netcraftsmen.pangea.intel:
        token: '{{ token }}'
        domain: '{{ domain }}'
        action: domain
        parameters:
          domain: "737updatesboeing.com"
          provider: domaintools

    - name: URL reputation
      netcraftsmen.pangea.intel:
        token: '{{ token }}'
        domain: '{{ domain }}'
        action: url
        parameters:
          url: http://113.235.101.11:54384
          provider: crowdstrike


RETURN VALUES:
- changed
        did the module change the remote server
        returned: always
        type: bool

- data
        data returned from the API call of the requested action
        returned: success
        type: dict

- fail
        for internal use, indicates if module.fail is to be called
        returned: always
        type: bool

- msg
        an error message or other information returned as to the
        status
        returned: optional
        sample: 'Url Intel Error: Not authorized to access this resource []'
        type: str

```

## Author

Joel W. King (@joelwking)