import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/samzwen/')

bit = platform.architecture()[0]
if bit == '64bit':
    import data64
elif bit == '32bit':
    import data32
