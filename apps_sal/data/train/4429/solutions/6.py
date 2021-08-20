from collections import Counter


def longest_palindrome(string):
    (possibles, has_odd) = (0, False)
    for (char, c) in Counter(string.lower()).items():
        if not char.isalnum():
            continue
        if c & 1:
            possibles += c - 1
            has_odd = True
        else:
            possibles += c
    return possibles + (1 if has_odd else 0)
