## Basic Debugging

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

## Author 

Joel W. King (@joelwking)
