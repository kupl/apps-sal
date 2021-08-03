from collections import Counter
from itertools import accumulate
from operator import add
from string import ascii_lowercase


def solve(s, n):
    counter = Counter(s)
    cum_count = [0] + list(accumulate((counter[c] for c in ascii_lowercase), add))
    result = []
    for c in s:
        cum_count[ord(c) - 97] += 1
        if cum_count[ord(c) - 97] > n:
            result.append(c)
    return "".join(result)
