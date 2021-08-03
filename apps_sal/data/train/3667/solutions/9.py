
def mid_endian(n):
    s = '{:0X}'.format(n)
    s = '0' * (len(s) % 2) + s
    ret = ''
    for n, i in enumerate([s[i * 2: (i + 1) * 2] for i in range(len(s) // 2)]):
        ret = i + ret if n % 2 == 1 else ret + i
    return ret
