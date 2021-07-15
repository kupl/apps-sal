def tv_remote(word):
    word, total = 'a' + word, 0
    s = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    d = {i: (s.index(i)//8, s.index(i)%8) for i in s}
    
    for a, b in zip(word, word[1:]):
        (x1, y1), (x2, y2) = d[a], d[b]
        total += abs(x1 - x2) + abs(y1 - y2)
    return total + len(word) - 1
