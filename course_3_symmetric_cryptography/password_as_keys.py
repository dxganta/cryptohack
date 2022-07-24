import hashlib
import random
import requests
from Crypto.Cipher import AES


URL = 'http://aes.cryptohack.org/passwords_as_keys/decrypt'
ciphertext = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}
    

with open("./words") as f:
    words = [w.strip() for w in f.readlines()]
    n = len(words)
    for i in range(n):

        word = words[i]

        KEY = hashlib.md5(word.encode()).digest().hex()

        ans = decrypt(ciphertext, KEY)['plaintext']

        try: 
            print(bytearray.fromhex(ans).decode())
        except:
            pass

        


        # url = f'{URL}/{ciphertext}/{KEY}/'
        # r = requests.get(url)

        # if bytes.fromhex(r.json()['plaintext'])[0] == 'c':
        #     print(url)