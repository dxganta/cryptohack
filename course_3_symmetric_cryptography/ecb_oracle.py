from pydoc import plain
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from requests import get

URL = 'http://aes.cryptohack.org/ecb_oracle/encrypt/'


KEY = b'herogiriherogiri'
FLAG = b'crypto{mY_TeSt_fLAg}'.hex()

def to_hex_int(x):
    return hex(x)[2:].zfill(2)

def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return encrypted.hex()

def encrypt_req(plaintext):
    url = f'{URL}{plaintext}'

    r = get(url)

    return r.json()['ciphertext']


# ciphertext is in hex
def first_block_in_bytes(ciphertext):
    return bytes.fromhex(ciphertext)[:16]

def second_block_in_bytes(ciphertext):
    return bytes.fromhex(ciphertext)[16:32]

# prev_ans = b'crypto{p3n6u1n5'
ans = b'crypto{p3n6u1n5'
# ans = b'crypto{mY_TeSt_'
while len(ans) < 32:
    print(len(ans), ans)

    plaintext = bytearray(31 - len(ans))

    expected_ciphertext = encrypt_req(plaintext.hex())
    expected_ciphertext_second_block = second_block_in_bytes(expected_ciphertext)
    assert(len(expected_ciphertext_second_block) == 16)

    plaintext += ans 
    assert(len(plaintext) == 31)

    for i in range(256):
        print(i)
        i_in_bytes = bytes.fromhex(to_hex_int(i))
        new_plaintext = plaintext + i_in_bytes
        assert len(new_plaintext) == 32
        cipher_second_block = second_block_in_bytes(encrypt_req(new_plaintext.hex()))

        if (cipher_second_block == expected_ciphertext_second_block):
            # i is in fucking hex when we get the answer
            ans += i_in_bytes
            # plaintext = bytearray(15 - len(ans))
            # plaintext += ans
            # assert(len(plaintext) == 15)

            break
