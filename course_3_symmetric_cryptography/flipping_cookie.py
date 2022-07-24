from Crypto.Cipher import AES
from requests import get
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta

def xor_hexes(a, b) -> str:
    return hex(int(a, 16) ^ int(b, 16))[2:]

cookie_encrypted = "45f4ed7a1fda115ed1d6b988c25b9e5cc038c5fe94187f8d9518ef04b9e3952d32d07a2984328da7a7eea4e4960d45ed"
ciphertext_bytes = bytes.fromhex(cookie_encrypted)[16:]
ciphertext_hex = ciphertext_bytes.hex()
iv = (bytes.fromhex(cookie_encrypted)[:16]).hex()

cookie = f"admin=False;expiry={123456789}".encode()

plaintext_first_block = cookie[:16].hex()

decrypted_first_block = xor_hexes(plaintext_first_block, iv)

to_want_cookie = b'admin=True;expir'.hex()

ans_iv = xor_hexes(decrypted_first_block, to_want_cookie)

print(ciphertext_hex)
print(ans_iv)
