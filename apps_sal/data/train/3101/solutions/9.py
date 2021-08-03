def palindrome_pairs(a):
    a = [str(x) for x in a]
    r = []
    for k1, i in enumerate(a):
        for k2, j in enumerate(a):
            if i != j and (i + j) == (i + j)[::-1]:
                r.append([k1, k2])
    return r
