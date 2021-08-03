from collections import Counter


def longest_palindrome(s):
    d, r = Counter([x for x in s.lower() if x.isalnum()]), 0
    for x in d.values():
        r += x // 2 * 2 + (x % 2 >> r % 2)
    return r
