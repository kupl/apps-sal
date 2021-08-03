def switch_endian(n, bits):
    if 2**bits <= n or bits % 8 != 0 or bits < 8:
        return None
    xn = bits // 4
    x = format(n, 'x').zfill(xn)
    lst = [x.upper()[i:i + 2] for i in range(0, len(x), 2)]
    s = ''.join(lst[::-1])
    ans = int(s, 16)
    return ans if len(bin(ans)[2:]) <= bits else None
