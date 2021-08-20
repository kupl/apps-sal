from collections import Counter


def permute_a_palindrome(s):
    return sum((1 for c in Counter(s).values() if c % 2)) < 2
