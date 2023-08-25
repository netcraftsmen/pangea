## Basic Debugging

We encountered issues with the certificate chain present on the development laptop 23 August 2023. The Cisco Umbrella Root CA on my laptop was causing the problem, assumed the Advanced Cisco Umbrella SSL Decryption feature. These notes are from the debugging session

### Code snippit

This is a minimal piece of Python code invoking the SDK/API. Needed is the domain and token, which is set on `console.pangea.cloud`.

Refer to the Python code examples <https://github.com/pangeacyber/pangea-python/tree/main/examples> for examples of the SDK usage.

```python
import os

import pangea.exceptions as pe
from pangea.config import PangeaConfig
from pangea.services import UserIntel

token = os.getenv("PANGEA_INTEL_TOKEN")
domain = os.getenv("PANGEA_DOMAIN")
config = PangeaConfig(domain=domain)
intel = UserIntel(token, config=config)
response = intel.user_breached(email="test@example.com", provider="spycloud", verbose=False, raw=True)
```

## OpenSSL

Debug SSL connectivity with s_client commands to check whether the certificate is valid, trusted, and complete.

`openssl s_client -connect user-intel.aws.us.pangea.cloud:443`

## Test ciphers

From: <https://superuser.com/questions/109213/how-do-i-list-the-ssl-tls-cipher-suites-a-particular-website-offers>

```bash
#!/usr/bin/env bash
    
# OpenSSL requires the port number.
SERVER=$1
DELAY=1
ciphers=$(openssl ciphers 'ALL:eNULL' | sed -e 's/:/ /g')
    
echo Obtaining cipher list from $(openssl version).
    
for cipher in ${ciphers[@]}
do
  echo -n Testing $cipher...
  result=$(echo -n | openssl s_client -cipher "$cipher" -connect $SERVER 2>&1)
  if [[ "$result" =~ ":error:" ]] ; then
    error=$(echo -n $result | cut -d':' -f6)
    echo NO \($error\)
  else
    if [[ "$result" =~ "Cipher is ${cipher}" || "$result" =~ "Cipher    :" ]] ; then
      echo YES
    else
      echo UNKNOWN RESPONSE
      echo $result
    fi
  fi
  sleep $DELAY
done
```

### Generate MD5 hash

```shell
echo -n 'cisco123' | md5sum
echo -n 'cisco123' | sha1sum
```

The hashtype is one of ['MD5', 'SHA1', 'SHA256']  (lowercase) Only specify the first 5 characters

```python
from pangea.services.intel import HashType
# only HashType only returns a string
HashType.MD5
response = intel.password_breached(hash_prefix="7b3c80"[:5], hash_type='md5', provider="spycloud")
```

## Author 

Joel W. King (@joelwking)
