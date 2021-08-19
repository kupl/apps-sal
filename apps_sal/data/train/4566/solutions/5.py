def counting_valleys(s):
    r = l = 0
    for x in s:
        if x == 'U' and l == -1:
            r += 1
        if x != 'F':
            l += 1 if x == 'U' else -1
    return r
