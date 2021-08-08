from cryptography.fernet import Fernet
import os
#with open('filekey.key', 'rb') as filekey:
#    key = filekey.read()
key = os.environ["key"]
# using the generated key
fernet = Fernet(key)
  
# opening the original file to encrypt
with open('test.txt', 'rb') as file:
    original = file.read()
      
# encrypting the file
encrypted = fernet.encrypt(original)
with open('crypt_test.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)