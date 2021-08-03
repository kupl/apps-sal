from collections import Counter


def missing_alphabets(s):
    c, a = Counter(s), Counter(map(chr, range(97, 123)))
    return ''.join(sorted((sum([a] * max(c.values()), Counter()) - c).elements()))
