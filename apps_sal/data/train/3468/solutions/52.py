# Tests whether a portion of s1 can be rearranged to match s2

from collections import Counter


def scramble(s1, s2):

    count_letters = Counter(s1)
    count_letters.subtract(Counter(s2))
    return (all(n >= 0 for n in count_letters.values()))
