D = {v: (r, c) for (r, row) in enumerate(['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/']) for (c, v) in enumerate(row)}


def tv_remote(word):
    return sum((abs(D[a][0] - D[b][0]) + abs(D[a][1] - D[b][1]) + 1 for (a, b) in zip('a' + word, word)))
