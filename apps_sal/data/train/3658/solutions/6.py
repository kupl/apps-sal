def swap(s, n):
    (bits, r, c) = (bin(n)[2:], '', 0)
    for i in s:
        r += [i, i.swapcase()][int(bits[c % len(bits)])]
        c += i.isalpha()
    return r
