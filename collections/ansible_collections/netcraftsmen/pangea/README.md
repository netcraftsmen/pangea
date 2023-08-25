# Ansible Collection - blueally.pangea aka, netcraftsmen.pangea

Documentation for the collection.

## Installation

The collection is installed like all Ansible Content Collections.

```shell
ansible-galaxy collection install netcraftsmen.pangea
```

## Token and Domain

Determine the `domain` value from the Pangea Cloud [Console](https://console.pangea.cloud/) home page. An example is `aws.us.pangea.cloud`.  Authentication is through the use of Bearer Tokens. Each service can have a unique Bearer Token, or you can create a single token associated with multiple services. The token can be encrypted with `ansible-vault` and stored in a host or group vars file, or set in an environment variable. Manage the project tokens from the `https://console.pangea.cloud/project/tokens` page.

## Plugins

The following plugins are included in the collection:

| Name | Type | Description |
|-|- |- |
| pangea.intel | module | User Intel, URL and Domain Plugin |

### pangea.intel

The intel plugin module implements these features of the Pangea service. The `action` parameter specifies the action to perform, "user", "url", "domain" and "password".

The `parameter` parameter, specifies a dictionary of key, value pairs, providing one or more parameters for the given action. For example, to provide User IP intel, the parameters could be as shown:

```yaml
parameters:
  ip: '192.0.2.1'
  raw: true
  verbose: true
  start: "2022-05-15"
  end: "2023-01-15"
```

The module will fail, or ignore parameters, that are incorrect or out of context.

#### User Intel
This module provides User Intel functionality to determine if an email address, username, phone number, password or IP address was exposed in a security breach.

#### Domain Intel

The Domain Intel service retrieves intelligence about known domain names, providing insight into the reputation of a domain. 

#### URL Intel

The URL Intel service retrieves intelligence about the reputation of a URL.

## Documentation

Review the `intel` module documentation, issue:

```shell
ansible-doc netcraftsmen.pangea.intel
```

## Usage

The module documentation contains various execution examples, basic usage is shown:

```yaml
- name: User Intel module from the Pangea collection
  connection: local
  hosts: localhost
  gather_facts: false

  vars: 
    token: "{{ lookup('ansible.builtin.env', 'PANGEA_TOKEN') }}"
    domain: "{{ lookup('ansible.builtin.env', 'PANGEA_DOMAIN') }}"

  collections:
    - netcraftsmen.pangea

  tasks:
    - name: User Intel email
      intel:
        token: '{{ token }}'
        domain: '{{ domain }}'  # aws.us.pangea.cloud
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