LAYOUT = 'a   b   c   d   e   1   2   3\nf   g   h   i   j   4   5   6\nk   l   m   n   o   7   8   9\np   q   r   s   t   .   @   0\nu   v   w   x   y   z   _   /\n'.split()


def get_pos(char):
    return divmod(LAYOUT.index(char), 8)


def distance(char1, char2):
    (c1x, c1y) = get_pos(char1)
    (c2x, c2y) = get_pos(char2)
    return abs(c1x - c2x) + abs(c1y - c2y)


def tv_remote(word):
    return sum((distance(prev, curr) for (prev, curr) in zip('a' + word, word))) + len(word)
