from collections import Counter


def freq_seq(string, separator):
    count = Counter(string)
    return separator.join((str(count[symbol]) for symbol in string))
