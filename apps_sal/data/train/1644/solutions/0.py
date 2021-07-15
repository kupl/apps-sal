from math import ceil
def b91decode(strng):
    ret = ''
    base91_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
    '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
    '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']
    strng_arr = [strng[i:i+2] for i in range(0, len(strng), 2)]
    origin_bin = ''
    for str in strng_arr:
        num = 0
        if len(str) == 1:
            num += base91_alphabet.index(str[0])
            origin_bin = bin(num)[2:] + origin_bin
        else:
            num += base91_alphabet.index(str[0])
            num += base91_alphabet.index(str[1])*91
            if num & 8191 > 88:
                origin_bin = bin(num)[2:].zfill(13) + origin_bin
            else:
                origin_bin = bin(num)[2:].zfill(14) + origin_bin
    origin_bin = origin_bin.zfill(int(ceil(len(origin_bin)/8.0))*8)
    ret = [origin_bin[i:i+8] for i in range(0, len(origin_bin), 8)]
    return ''.join(map(lambda x:chr(int(x, 2)), ret))[::-1]
        
            
            
    
def b91encode(strng):
    base91_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
    '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
    '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']
    ret = ''
    strng_bin = map(lambda x:bin(ord(x))[2:].zfill(8), list(strng))
    strng_bin_r = ''
    for i in range(len(strng_bin)):
        strng_bin_r = strng_bin[i] + strng_bin_r
    strng_bin_r = strng_bin_r[::-1]
    index = 0
    while index < len(strng_bin_r):
        num = int(strng_bin_r[index:index+13][::-1], 2)
        if num > 88:
            index += 13
            ret += base91_alphabet[num%91] + base91_alphabet[num/91]
        else:
            num = int(strng_bin_r[index:index+14][::-1], 2)
            index += 14
            ret += base91_alphabet[num%91] + base91_alphabet[num/91]
    ret = ret[0:len(ret)-2]
    if num > 90:
        ret += base91_alphabet[num%91] + base91_alphabet[num/91]
    else:
        ret += base91_alphabet[num%91]
    return ret
