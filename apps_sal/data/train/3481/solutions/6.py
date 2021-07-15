from itertools import groupby
from collections import defaultdict
def get_char_count(s):
    d = defaultdict(list)
    for k, g in groupby(filter(str.isalnum, sorted(s.lower()))):
        d[len(list(g))].append(k)
    return d
