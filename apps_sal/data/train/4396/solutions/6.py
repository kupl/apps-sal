from collections import Counter


def freq_seq(string, sep):
    counter = Counter(string)
    return sep.join((str(counter[char]) for char in string))
