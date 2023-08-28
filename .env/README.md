## .env

### Environment variables

Store your credentials in a file `login.sh` in this directory. Tokens can be unique to a service or shared across multiple services. The playbooks are set up to use a shared token, but could be modified easily.

```shell
export PANGEA_TOKEN=token
export PANGEA_AUDIT_TOKEN=$PANGEA_TOKEN
export PANGEA_DOMAIN=aws.us.pangea.cloud
```

If you wish to send a demonstration email using Gmail, you must provide a Gmail account and app token.

```shell
export GMAIL_TOKEN=token
export GMAIL_USERNAME=account@gmail.com
```

otherwise, use `--skip-tags sendmail` to avoid sending an email.

From your container, you can `source .env/login.sh` to set the variables in your terminal window

### Ansible Vault Password

Refer to `playbooks/ansible.cfg`, you can specify your vault password in `vault_password.txt` to avoid having to specify `--ask-vault-password` on the command line.