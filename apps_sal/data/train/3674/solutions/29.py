def add_binary(a, b):
    res = a + b
    buf = ''
    while res >= 1:
        buf += str(res % 2)
        res = res // 2
    buf = buf[::-1]
    return buf
