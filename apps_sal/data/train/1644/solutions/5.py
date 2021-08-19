from itertools import zip_longest as lzip

b91abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'


def b91decode(string):
    b = ''
    for x, y in lzip(*[iter(string)] * 2):
        num = 0
        if y is None:
            num += b91abc.index(x)
            b = bin(num)[2:] + b
        else:
            num += b91abc.index(x) + b91abc.index(y) * 91
            b = bin(num)[2:].zfill(13 if num & 8191 > 88 else 14) + b
    b = b.zfill((len(b) // 8 + 1) * 8)
    return ''.join(chr(int(''.join(x), 2)) for x in lzip(*[iter(b)] * 8, fillvalue=''))[::-1]


def b91encode(string):
    ret = b = ''
    index = num = 0
    for x in string:
        b = bin(ord(x))[2:].zfill(8) + b
    b = b[::-1]
    while index < len(b):
        num = int(b[index:index + 13][::-1], 2)
        if num <= 88:
            num = int(b[index:index + 14][::-1], 2)
            index += 1
        index += 13
        ret += b91abc[num % 91] + b91abc[num // 91]
    return ret[:len(ret) - 2] + b91abc[num % 91] + b91abc[num // 91] * (num > 90)
