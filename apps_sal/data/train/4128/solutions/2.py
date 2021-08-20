from regex import findall


def bears(x, s):
    res = findall('(B8|8B)', s)
    return [''.join(res), len(res) >= x]
