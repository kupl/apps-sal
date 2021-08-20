from collections import Counter, defaultdict
from bisect import insort


def get_char_count(s):
    D = defaultdict(list)
    for (k, v) in Counter(map(str.lower, filter(str.isalnum, s))).items():
        insort(D[v], k)
    return D
