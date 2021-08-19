def tv_remote(word):
    t = ['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']
    r = 0
    pos = (0, 0)
    for x in word:
        for i in range(5):
            if x in t[i]:
                r += abs(pos[1] - t[i].index(x)) + 1 + abs(pos[0] - i)
                pos = (i, t[i].index(x))
    return r
