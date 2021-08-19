def add_binary(a, b):
    sum = a + b
    res = ''
    while sum > 0:
        if sum & 1:
            res = '1' + res
        else:
            res = '0' + res
        sum = sum >> 1
    return res
