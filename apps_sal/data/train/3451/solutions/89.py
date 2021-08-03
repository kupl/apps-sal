from math import ceil


def memoize(f):
    memo = {}

    def _(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return _


@memoize
def reduce(row):
    MAP = {'RR': 'R', 'GG': 'G', 'BB': 'B', 'RG': 'B', 'RB': 'G', 'GR': 'B', 'GB': 'R', 'BR': 'G', 'BG': 'R'}
    CHUNK = 16
    len_ = len(row)
    if len_ == 1:
        return row
    elif len_ == 2:
        return MAP[row]
    elif len_ > CHUNK + 1:
        n = ceil(len_ / CHUNK)
        return ''.join([reduce(row[CHUNK * i:CHUNK * (i + 1) + 1]) for i in range(n)])
    else:
        return ''.join([MAP[row[i:i + 2]] for i in range(len_ - 1)])


def triangle(row):
    while len(row) > 1:
        row = reduce(row)
    return row
