def xor(a, b):
    '''
        a & b are integers
    '''
    return a ^ b


def xorString(x):
    '''
        xors the ascii number of each character with 13, converts it to a character again and returns the string
    '''
    ans= ''
    for i in x:
        ans += chr(xor(ord(i), 13))

    return ans

if __name__ == '__main__':
    x = 'label'
    print(xorString(x))
