from collections import Counter


def palindrome_rearranging(s):
    return len([v for v in Counter(s).values() if v % 2]) < 2
