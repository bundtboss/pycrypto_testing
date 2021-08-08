from cryptography.fernet import Fernet
import os

# with open('filekey.key', 'rb') as filekey:
#     key = filekey.read()
key = os.environ["key"]  
# using the generated key
fernet = Fernet(key)
  
# opening the original file to encrypt
with open('crypt_test.txt', 'rb') as file:
    crypt = file.read()
      
# encrypting the file
decrypt = fernet.decrypt(crypt)
  
# opening the file in write mode and 
# writing the encrypted data
with open('crypt_test.txt', 'wb') as encrypted_file:
    encrypted_file.write(decrypt)