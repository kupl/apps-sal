from itertools import cycle, islice


def get_a_down_arrow_of(n):

    r = []

    for i, x in enumerate(range(n, 0, -1)):
        c = cycle('1234567890')
        s = list(islice(c, x))
        s += s[::-1][1:]
        r.append(' ' * i + ''.join(s))

    return '\n'.join(r)
