from collections import Counter


def longest_palindrome(s):
    freq = Counter((c for c in s.lower() if c.isalnum()))
    (even, odd) = ([], [])
    for (k, v) in freq.items():
        if v % 2:
            odd.append(v - 1)
        else:
            even.append(v)
    return sum(even) + (sum(odd) + 1 if odd else 0)
