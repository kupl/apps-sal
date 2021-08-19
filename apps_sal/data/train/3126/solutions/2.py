def palindrome_rearranging(s):
    d = {}
    c = 0
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for (k, v) in d.items():
        if v % 2 != 0:
            c += 1
    return c <= 1
