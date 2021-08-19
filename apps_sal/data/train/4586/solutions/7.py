def tv_remote(word):
    k = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    (P, sum) = (0, 0)
    for c in word:
        p = k.find(c)
        sum += abs(P // 8 - p // 8) + abs(P % 8 - p % 8) + 1
        P = p
    return sum
