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

## Author 

Joel W. King (@joelwking)