from Crypto.Cipher import AES
from requests import get

URL = 'http://aes.cryptohack.org/symmetry/encrypt/'

ciphertext = "2fddb0e8d5565684fce0829f30e8e7ec975db7e2e53aa7a0ffd71d881be5b4740fa0fd560ca1f5f60cad57aee2eeb2f39e"
encrypted_bytes = bytes.fromhex(ciphertext)[16:]
encrypted_hex = encrypted_bytes.hex()
iv = (bytes.fromhex(ciphertext)[:16]).hex()

def encrypt_req(plaintext, iv):
    url = f'{URL}{plaintext}/{iv}'
    r = get(url)

    return r.json()['ciphertext']

def xor_hexes(a, b) -> str:
    return hex(int(a, 16) ^ int(b, 16))[2:]

demo_plaintext = b'crypto{mytest_g}'.hex()

demo_ciphertext = encrypt_req(demo_plaintext, iv)

encrypted_first_block = xor_hexes(demo_ciphertext, demo_plaintext)

ciphertext_first_block = encrypted_bytes[:16].hex()

ans1 = bytes.fromhex(xor_hexes(encrypted_first_block, ciphertext_first_block))

demo_ciphertext_second_block = encrypt_req(demo_plaintext, encrypted_first_block)
encrypted_second_block = xor_hexes(demo_ciphertext_second_block, demo_plaintext)
ciphertext_second_block = encrypted_bytes[16:32].hex()

ans2 = bytes.fromhex(xor_hexes(ciphertext_second_block, encrypted_second_block))

print(ans1+ans2)