def convert(n):
    s = str(n)[::-1]
    p = [s[i::4].count('1') for i in range(4)]
    return [p[0] - p[2], p[1] - p[3]]
