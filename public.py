import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from public import file
    login()
elif bit == '32bit':
    from public import file
    login()