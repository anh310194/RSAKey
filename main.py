from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP


message = 'To be encrypted'
key = RSA.importKey(open('mykey.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)

listTestByte = list(ciphertext)
print(listTestByte)

random_generator = Random.new().read
key =   RSA.generate(1024, random_generator) #generate pub and priv key
keyp = PKCS1_OAEP.new(key)

publickey = key.publickey() # pub key export for exchange

print(publickey)

encrypted =  publickey.encrypt('encrypt this message',32)

print('encrypted message:', encrypted) #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryption.txt', 'r')
message = f.read()


decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print('decrypted', decrypted)

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()
# key = RSA.generate(2048)
# f = open('mykey.pem','wb')
# f.write(key.export_key('PEM'))
# f.close()

# f = open('mykey.pem','r')
# key = RSA.import_key(f.read())