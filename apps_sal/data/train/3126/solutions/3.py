from collections import Counter


def palindrome_rearranging(s):
    return sum(v % 2 for v in Counter(s).values()) < 2
