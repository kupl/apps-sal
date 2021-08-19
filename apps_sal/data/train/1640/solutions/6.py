from collections import Counter


def mix(s1, s2):
    (c1, c2) = [Counter({s: n for (s, n) in Counter(c).items() if n > 1 and s.islower()}) for c in (s1, s2)]
    return '/'.join((c + ':' + -n * s for (n, c, s) in sorted(((-n, '=12'[(c1[s] == n) - (c2[s] == n)], s) for (s, n) in (c1 | c2).items()))))
