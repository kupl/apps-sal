from itertools import cycle
one = '   _( )__\n _|     _|\n(_   _ (_\n |__( )_|'.splitlines()
rev = ' |_     |_\n  _) _   _)\n |__( )_|'.splitlines()


def puzzle_tiles(n, m):
    (build, it) = (one.copy(), [2, 3, 2, 2])
    for i in range(n - 1):
        for j in range(len(build)):
            build[j] += one[j][it[j]:]
    (build_rev, it) = (rev.copy(), [3, 4, 2])
    for i in range(n - 1):
        for j in range(len(build_rev)):
            build_rev[j] += rev[j][it[j]:]
    nex = cycle([build[1:], build_rev])
    return '\n'.join([build[0]] + sum([next(nex) for i in range(m)], []))
