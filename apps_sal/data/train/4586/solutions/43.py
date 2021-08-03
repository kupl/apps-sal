def tv_remote(word):
    keys = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    p, c = (0, 0), 0
    for s in word:
        for i, row in enumerate(keys):
            for j, v in enumerate(row):
                if v == s:
                    c += abs(p[0] - i) + abs(p[1] - j) + 1
                    p = (i, j)
    return c
