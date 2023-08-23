# Ansible Collection - blueally.pangea (aka, netcraftsmen.pangea)

Documentation for the collection.

## Installation

The collection is installed like all Ansible Content Collections.

```shell
ansible-galaxy collection install blueally.pangea
```

## Token and Domain

Determine the `domain` value from the Pangea Cloud [Console](https://console.pangea.cloud/) home page. An example is `aws.us.pangea.cloud`.  Authentication is through the use of Bearer Tokens. Each service can have a unique Bearer Token, or you can create a single token associated with multiple services. The token can be encrypted with `ansible-vault` and stored in a host or group vars file, or set in an environment variable. Manage the project tokens from the `https://console.pangea.cloud/project/tokens` page.


## Documentation

Review the `intel` module documentation, issue:

```shell
ansible-doc blueally.pangea.intel
```

The module documentation contains various execution examples, basic usage is shown:

```yaml
- name: Functional test of the Pangea collection
  connection: local
  hosts: localhost
  gather_facts: false

  vars: 
    token: "{{ lookup('ansible.builtin.env', 'PANGEA_TOKEN') }}"
    domain: "{{ lookup('ansible.builtin.env', 'PANGEA_DOMAIN') }}"

  collections:
    - blueally.pangea

  tasks:
    - name: User Intel email
      intel:
        token: '{{ token }}'
        domain: aws.us.pangea.cloud
        logger: false
        action: user
        parameters:
          email: "info@blueally.com"
          raw: true
      register: pangea
      tags: ['email']

```

## Author

Joel W. King @joelwking