def convert(n):
    s = str(n)[::-1]
    return [sum(p * s[i - p::4].count("1") for p in (1, -1)) for i in (1, 2)]
