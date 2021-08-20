from collections import Counter
import re


def longest_palindrome(s):
    (n, odds, c) = (0, 0, Counter(re.sub('\\W+|_', '', s.lower())))
    for v in c.values():
        (x, r) = divmod(v, 2)
        n += 2 * x
        odds += r
    return n + bool(odds)
