keyboard = ("abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/", "
D={c: (i, j) for i, row in enumerate(keyboard) for j, c in enumerate(row)}


def tv_remote(words):
    i=j=up=res=0
    for c in words:
        if c.isalpha() and c.isupper() != up:
            k, l=D['
            res += abs(i - k) + abs(j - l) + 1
            i, j, up=k, l, 1 - up
        k, l=D[c.lower()]
        res += abs(i - k) + abs(j - l) + 1
        i, j=k, l
    return res
