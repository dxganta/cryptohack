from hexToBytes import hexToBytes
from Crypto.Util.number import *

def xor(a,b):
    '''
        a is hex, b is int
    '''

    return hexToInt(a) ^ b

def hexToInt(hex):
    return int(hex,16)

if __name__ == '__main__':
    x ='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
    # convert x to int then xor with a bit then convert it to hex and then byte and print it
    print(hexToBytes(x))
    key = 0
    ans = b''
    byts = hexToBytes(x)
    i = 0
    while key == 0:
        temp = b''
        for j in range(2):
            temp += long_to_bytes(byts[j] ^ i)
        if temp == b'cr':
            key = i
        i += 1
            

    for byt in byts:
        ans += long_to_bytes(byt ^ key)

    print("Your answer is", ans)
   