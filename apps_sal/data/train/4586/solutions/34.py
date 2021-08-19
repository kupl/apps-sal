def tv_remote(word):
    keys = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    (res, last) = (len(word), 0)
    for c in word:
        i = keys.index(c)
        res += abs(i % 8 - last % 8) + abs(i // 8 - last // 8)
        last = i
    return res
