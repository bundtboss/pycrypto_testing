import base64
import os
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = getpass.getpass(prompt="Password")
password = bytes(password,'utf-8')
salt = os.urandom(16)
kdf = PBKDF2HMAC(
algorithm=hashes.SHA512_224(),
length=32,
salt=salt,
iterations=100000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))

# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)