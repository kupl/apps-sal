def tv_remote(word):
    keys = ['-afkpu', '-bglqv', '-chmrw', '-dinsx', '-ejoty', '-147.z', '-258@_', '-3690/']
    index_last = first_in(word[0], keys)
    ret = sum(index_last)
    for i in word[1:]:
        inkey = first_in(i, keys)[0]
        ret += abs(index_last[0] - inkey) + abs(index_last[1] - first_in(i, keys[inkey])[0]) + 1
        index_last = [inkey, first_in(i, keys[inkey])[0]]
    return ret


def first_in(l, k):
    return [(k.index(e), e.index(l)) for e in k if l in e][0]
