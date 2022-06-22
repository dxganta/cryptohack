#  Before you XOR these objects, be sure to decode from hex to bytes.

from hexToBytes import hexToBytes


def xor(a,b):
    '''
        a & b are in hex
    '''

    return hex(hexToInt(a) ^ hexToInt(b))

def hexToInt(hex):
    return int(hex,16)

def intToHex(int):
    return hex(int)

if __name__ == "__main__":
    key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
    key2_key1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
    key2_key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
    flag_key1_key3_key2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

    print(xor(xor(key1, key2_key3), flag_key1_key3_key2))

    print(hexToBytes("63727970746f7b7830725f69355f61737330633161743176337d"))