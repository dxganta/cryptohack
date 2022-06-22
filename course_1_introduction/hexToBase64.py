import base64
from hexToBytes import hexToBytes

'''
    hex to base64 encoding
'''

def hexToBase64(hexString):
    '''
        hex to base64 encoding
    '''
    return base64.b64encode(hexToBytes(hexString))


if __name__ == '__main__':
    hexStr = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
    print(hexToBase64(hexStr))