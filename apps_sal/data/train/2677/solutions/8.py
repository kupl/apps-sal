import re
D = {v: [r, c] for r, row in enumerate(['abcde123', 'fghij456', 'klmno789', 'pqrst.@0', 'uvwxyz_/', '* ']) for c, v in enumerate(row)}


def manhattan_dist(*points):
    print('points md: ', points)
    return [abs(z2 - z1) for z1, z2 in zip(*points)]


def wrap_manhattan_dist(*points):
    dist = manhattan_dist(*points)
    wdist = [min(dist[0], 6 - dist[0]), min(dist[1], 8 - dist[1])]
    return sum(wdist)


def tv_remote(words):
    words = re.sub('([A-Z])', r'*\1*', words).lower()
    words = re.sub('\*([\d.@_/ ]*)(\*|$)', r'\1', words)
    words = re.sub('\*$', '', words)
    words = re.sub('\*([0-9.@_/ ]+)([^\*])', r'\1*\2', words)
    words = 'a' + words
    moves = sum([wrap_manhattan_dist(D[words[i]], D[words[i + 1]]) + 1 for i in range(len(words) - 1)])
    return moves
