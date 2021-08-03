def count_deaf_rats(town):
    twn = town.replace(' ', '').split('P')
    return sum(find_d(e, [['O', '~'], ['~', 'O']][i]) for i, e in enumerate(twn))


def find_d(r, w):
    r = [e for e in r]
    return sum([1 for i in range(0, len(r), 2) if r[i:i + 2] == w])
