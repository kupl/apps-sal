def thue_morse(n):
    k = t = 0
    while t.bit_length() < n:
        t = t << 2 ** k | ~t & (1 << 2 ** k) - 1
        k += 1
    return bin(t).replace('b', '')[:n]
