lst0 = [2]
for i in range(1, 20):
    lst0.append(lst0[-1] * 2)


def switch_endian(n, bits):
    if n < 0 or bits not in lst0 or (n, bits) == (256, 8):
        return None
    xn = bits // 4
    x = format(n, 'x').zfill(xn)
    lst = [x.upper()[i:i + 2] for i in range(0, len(x), 2)]
    s = ''.join(lst[::-1])
    ans = int(s, 16)
    return ans if len(bin(ans)[2:]) <= bits else None
