from pydoc import plain
from Crypto.Cipher import AES
from requests import get

ENCRYPT_URL = 'http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/'
DECRYPT_URL = 'http://aes.cryptohack.org/ecbcbcwtf/decrypt/'


cipher_text = '189ae557cdc362166ff0c8e026132d63e17fb02fc6ff2c265b3682af9c95d09274e76b7f207e52626225ef705b1e12f5'
plaintext = '7be89c27b9ac19250c9297d553704656be4bc61ff79b73176c69a38ebdb4f1ef'

def iv():
    return (bytes.fromhex(cipher_text)[:16]).hex()

def encrypted_in_bytes():
    return bytes.fromhex(cipher_text)[16:]

def encrypted_in_hex():
    return encrypted_in_bytes().hex()


def encrypt_req(plaintext):
    url = f'{ENCRYPT_URL}{plaintext}'

    r = get(url)

    return r.json()['ciphertext']


plaintext_first_block = (bytes.fromhex(plaintext)[:16]).hex()
plaintext_second_block = (bytes.fromhex(plaintext)[16:32]).hex()

ciphertext_first_block = encrypted_in_bytes()[:16].hex()

def xor_hexes(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:]

# answers
ans1 = xor_hexes(plaintext_first_block, iv())
ans1_b = bytes.fromhex(ans1)


ans2 = xor_hexes(ciphertext_first_block, plaintext_second_block)
ans2_b = bytes.fromhex(ans2)

print("FLAG", ans1_b + ans2_b)