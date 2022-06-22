from hexToBytes import hexToBytes
from Crypto.Util.number import *

def asciiStringToBytes(asciiStr):
    return bytes(asciiStr, 'ascii')

def intToAsciiString(int):
    s 
    

if __name__ == '__main__':
    x = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

    print(hexToBytes(x))
    ans = b''
    byts = hexToBytes(x)

    toCheck = 'crypto{'
    # key = bytes_to_long(byts[:precs]) ^ bytes_to_long(asciiStringToBytes(toCheck))
    # print(long_to_bytes(key))

    key = b'myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymy'
    precs = len(key)

    ans = long_to_bytes(bytes_to_long(byts) ^ bytes_to_long(key))

    print(ans)
    print(len(byts))

    # for byt in byts:
    #     ans += long_to_bytes(byt ^ key)
    # print(ans)
    # ans = b''

