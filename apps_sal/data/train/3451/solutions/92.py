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
    len_ = len(row)
    if len_ == 1:
        return row
    elif len_ == 2:
        return MAP[row]
    else:
        i = len_ // 2
        return reduce(row[0:i + 1]) + reduce(row[i:len_])


def triangle(row):
    while len(row) > 1:
        row = reduce(row)
    return row
