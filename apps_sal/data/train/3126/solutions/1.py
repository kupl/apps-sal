from collections import Counter


def palindrome_rearranging(s):
    return sum(n % 2 for n in Counter(s).values()) <= 1
