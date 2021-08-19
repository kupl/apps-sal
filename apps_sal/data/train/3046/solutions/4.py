def thue_morse(n):
    s = '0'
    while len(s) < n:
        s += ''.join([str(int(i) ^ 1) for i in s])
    return s[:n]
