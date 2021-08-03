from itertools import combinations


def subsequences(s):
    """Returns set of all subsequences in s."""
    return set(''.join(c) for i in range(len(s) + 1) for c in combinations(s, i))


def lcs(x, y):
    """Returns longest matching subsequence of two strings."""
    return max(subsequences(x).intersection(subsequences(y)), key=len)
