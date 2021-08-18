def tv_remote(word):
    pp = 0
    res = 0
    r = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    for w in word:
        p = r.find(w)
        res += abs(p // 8 - pp // 8) + abs(p % 8 - pp % 8) + 1
        pp = p
    return res
