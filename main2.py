from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from base64 import b64decode
import json



# keyPair = RSA.generate(2048)


public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzNnqm1jK4H+vvE5gKfe/hbtdFhns8LShB9cJiQD++M0u9BKA/eO4HLrocZXMb8r4Nh0UqdipO5EvN9cawIg8xDgu1OYcCEd/r422Brq/miHOFwYGPxWryCIfg++aF2CZFynCa/OGfzFiZ0xybo+VnRX0XTbLNk4jw4kAv16VmY2PQq7uyAGm0WMh+V0RCjIfy3N6jntmq8waAtdNmUweGX8ALAaFEdJpbuNpBKcmYl4knWCDPCmWi4AYSPP0g5wrujtZXhImS/4yypYYt9p1Ks7rBo8d/DKIbDLvJcquokbqWSUh/azBbfdZ1s+Nrrtc3NeiXsdBtx/zeUuopC4GtwIDAQAB"
keyDER = b64decode(public_key)
keyPub = RSA.importKey(keyDER)

json_data = {
    "farm_name":"anhnguyen-farm4",
    "agent_pool_id":"642403b37efc63937ebbba88",
    "databiz_queue":"databiz_6461e86012af4df8878c427c",
    "user_id": "641d682a4280a95d3da9168a", 
    "tenant_id": "641d68184280a95d3da91689"
    }

msg = json.dumps(json_data).encode('utf-8')
encryptor = PKCS1_OAEP.new(keyPub)
encrypted = encryptor.encrypt(msg)


print("Encrypted:", binascii.hexlify(encrypted))
print("--------------------------------")
