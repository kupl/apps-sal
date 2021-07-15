def longest(s1, s2):
    freq = {}
    for c in list(s1):
        freq[c] = freq.get(c, 0) + 1
    for c in list(s2):
        freq[c] = freq.get(c, 0) + 1
    l = sorted([c for c in list(freq.keys())])
    return ''.join(l)
