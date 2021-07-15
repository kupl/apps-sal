def to_bits(string):
    ret = [0] * 5000
    for i in string.split('\n'):
        ret[int(i)] = 1
    return ret
