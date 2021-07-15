def tv_remote(word):
    result = 0
    alpha = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    nxt = [0, 0]
    for c in word:
        i = alpha.index(c)
        where  = [i // 8, i % 8]
        result += abs(where[0] - nxt[0]) + abs(where[1] - nxt[1]) + 1
        nxt = where
    return result
