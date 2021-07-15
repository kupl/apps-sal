def to_bin(value):
    res = ''
    while value > 0:
        res += str(value % 2)
        value //= 2
    return ('{:0>4}'.format(res[::-1])) if res != '' else '0000'

def to_dec(value):
    res = 0
    
    value = value[::-1]
    for ix in range(len(value)):
        res += int(value[ix]) * (2 ** ix)

    return res

def hex_to_dec(s):
    convert = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'a' : 10,
        'b' : 11,
        'c' : 12,
        'd' : 13,
        'e' : 14,
        'f' : 15
    }
    
    res = list(map((lambda x:convert[x]), list(s)))
    res = list(map(to_bin, res))
    res = ''.join(res)
    
    return to_dec(res)
