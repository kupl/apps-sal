s = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'


def dx(c1, c2):
    return abs(s.index(c1) % 8 - s.index(c2) % 8)


def dy(c1, c2):
    return abs(s.index(c1) // 8 - s.index(c2) // 8)


def d(c1, c2):
    return 1 + dx(c1, c2) + dy(c1, c2)


def tv_remote(word, r=0):
    if r == 0:
        return tv_remote(word, d('a', word[0]))
    if len(word) == 1:
        return r
    else:
        return tv_remote(word[1:], r + d(word[1], word[0]))
