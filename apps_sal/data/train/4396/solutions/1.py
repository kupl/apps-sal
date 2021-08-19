from collections import Counter


def freq_seq(s, sep):
    freq = Counter(s)
    return sep.join((str(freq[c]) for c in s))
