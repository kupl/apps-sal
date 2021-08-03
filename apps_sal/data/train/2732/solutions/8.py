from string import ascii_letters as let, digits as dig


def blocks(s):
    if s:
        Max = max(map(s.count, s))
        bs = [''.join(sorted([c for c in set(s) if s.count(c) >= n + 1], key=(let + dig).find)) for n in range(Max)]
        return '-'.join(bs)
    else:
        return ''
