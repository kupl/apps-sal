from collections import Counter


def str_count(strng, letter):
    tot = Counter(strng)
    return tot[letter]
