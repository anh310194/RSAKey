from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from base64 import b64decode, b64encode
from Crypto.Util import asn1

ckd = '8d4e6ca434d8a489e164dd104512f56764717f18cc2d909a313505c78ef3a70ab2ea16ef4b523ce962d111afae348a45bb2592e9e337ab2bf282589e2cf94bd09142be1d764de16d257125ceb83a55ed6c2187200518d5865bf080abc41253329940bf0d0ba6058e2cd4dff374c6430f3a93934bd6bbb4b2c07d33d429848874eed4b7df61d07deb456a244ef74e140b872e201b5cbced5f551fdc4c98e129ae97fa820f71fd73c34e7b144af68d26669e02a5828f5c61bfc4eb329745f8859c12939be6d6b3b69e458adfba61c9ea7731a5650090cdd0ff5cc47e46d2bb910d6f6bb9efaecd52a9771c57fa9ef0122d744128fac5c3aa0970a9e313dcba3363'

# code_bytes  = ckd.encode('UTF-8')
# bbb = b'f\xd8\xf4\xe4;\xce\x1e\xe9\xcb\x03\x1f\x94\x95\xd0\x02\xaa\xe0\xc9Z\xff?A\xe7\xf43\xbf\xd1-T\\Z\xa1\xa8\xdfF\xfd\xf9\x8dm\xb6\xbc2\xf8}\xb8Y\xea+\xae\x03\xd5\xd7\xaak\x16\x99\xefV/<\xb5\xafv\xb9\xa3\xbd3\xf5w\x99\x88\x16\xcd\x8a\xb8\xfa@\xfayiWY\xaej\xa7\x97&\xde\xaa(\xb4-\xbcs\xc1\x04\xff\xfc\xff\xc7\xcag\xc4O#\xa1\x96\x97\x89\xf4h\x98\xac\xeff\xf7(\xa7T\xd3\x050\x13\xac\x03O\xf7\xbe'

encrypted= bytes.fromhex(ckd)
print(encrypted)



key64Private = 'MIIEpQIBAAKCAQEAzNnqm1jK4H+vvE5gKfe/hbtdFhns8LShB9cJiQD++M0u9BKA\
/eO4HLrocZXMb8r4Nh0UqdipO5EvN9cawIg8xDgu1OYcCEd/r422Brq/miHOFwYG\
PxWryCIfg++aF2CZFynCa/OGfzFiZ0xybo+VnRX0XTbLNk4jw4kAv16VmY2PQq7u\
yAGm0WMh+V0RCjIfy3N6jntmq8waAtdNmUweGX8ALAaFEdJpbuNpBKcmYl4knWCD\
PCmWi4AYSPP0g5wrujtZXhImS/4yypYYt9p1Ks7rBo8d/DKIbDLvJcquokbqWSUh\
/azBbfdZ1s+Nrrtc3NeiXsdBtx/zeUuopC4GtwIDAQABAoIBADB2HRpDFzuk+V4C\
7J0BDz4D5TGlUHhhQvcn2AmhQrB5WfJDrmBhztx9GyBD3+lSiwXCO3Ey4FZHMnRz\
XtDNahLBd9LF3TvYLkzJqZZN96Xu+WJY+oFSDyF5cRs1Q67kG1NvfZ8sLVVJyY3G\
eAvPzAUtfHHQ1KI0OiG394VOSvXYKrVXE8Cw7fU7kjZIBES3PHX/wZCnGPFUy8iZ\
ldFcZ6rchHFSa4tj7oomYYBPmEN3RROGMjBn98cGv8vkTXhsgK0qGKukmpVY6YYT\
2uCw75c3bSFI4Jg7cjsT5+8hoK5TY+DmMd9NzxsqDqymmGmL/ZqK3lWeXeK3sTwu\
CSQ46gECgYEA1JREMKUF22lC5GI0mph0vaTbYuZ7vTq6e5l9ZnO9sEvTI+6v0RZO\
6uyofVT3BhLgYypYxWVsHBCH4+snDjOl4m3/OsubNX7h1IzMCdUhZVVO3ZUwfcRK\
M5emQY65SSicqj9fdyJpwXQeXEwdD0+c9sFzKBZ5LPpwQyVgMUPbMfECgYEA9rGO\
yV5ZVw+6qzLcd0pzIGnCxCpdjhdIFuzUP7vX/SN2xQbNYEU7NNTXIPEwYYPO/C95\
xvn5UH2iwjFZS0l08nvgFcJT9vo6xMODPU7Yfuxebbpzd0AprX2Hm9bYEf30+s/l\
lq/wmVJ20EEqWizZl2cTOYxBmzEaF4/nJsLVGycCgYEAs6ciAeJVEtrgl1aPkl9p\
uaQLbIfQ51kspKxRGDaUhttt8x4TJCcwRsX+lv0pTs7BJ81v/FL8jLNDxNDEzvHD\
LZs8ahoMb6dtf04GWgDvGk6AOi+NLZyoAPYWoazW1gcmb5LjQTGqIr3ZsrL4lCn6\
Q2e1xJlJi0OTgIujwb7RDmECgYEA8FUE/UrMkNPDENxJCnJefHpsg72eTTqDQcpR\
8RFol7XAFKzO0nY/+vVL7EzszGOj9+2sntuTNwZe1P9MtdsHcuCZ67jZIiifrmem\
6MhyhBx01kOqD8hTkjBUN89zyvt1eg+l5UrchBJhq/uAbj95cFW71fm9RJruh3vr\
Psja4ksCgYEAq2O/hfdjyPX0kD+2CYcOXv9m2Kzk0YPeBQpReJtR4Dm9xP3FLuoU\
1Gfa4z5hVTRSWOTmElv8xJtJDcTpYpx9c/R2SgMXhJlwzoYKFVlryvUJFO03JvfQ\
vghqtTTUThVqSa7OkTxOh2/CQiRMtuWvQG9GOsqp04H7/Mb7YDCAxPw='
keyDERPrivate = b64decode(key64Private)
keyPrivate = RSA.importKey(keyDERPrivate)

decryptor = PKCS1_OAEP.new(keyPrivate)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)