def fusc(n):
    s = [1, 0]
    for i in map(int, bin(n)[2:]):
        s[i] += s[1 - i]
    return s[1]
