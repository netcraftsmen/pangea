## .env

### Environment variables

Store your credentials in a file `login.sh` in this directory.

```shell
export PANGEA_TOKEN=token
export PANGEA_DOMAIN=aws.us.pangea.cloud
```

From your container, you can `source .env/login.sh` to set the variables in your terminal window

### Ansible Vault Password

Refer to `playbooks/ansible.cfg`, you can specify your vault password in `vault_password.txt` to avoid having to specify `--ask-vault-password` on the command line.