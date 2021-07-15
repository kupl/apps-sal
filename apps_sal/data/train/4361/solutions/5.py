from collections import *

NUM_DIG = 8
palindromes = OrderedDict()
for n in range(int(10 ** (NUM_DIG / 2)) + 1):
    key = Counter(str(n ** 2))
    if '0' not in key:
        palindromes.setdefault(
            frozenset(key.most_common()), []).append(n ** 2)

lasts, lengths = {}, defaultdict(list)
for seq in palindromes.values():
    for n in seq:
        lengths[len(seq)].append(n)
        lasts[n] = seq[-1]
for k in lengths: lengths[k].sort()

from bisect import bisect
def next_perfectsq_perm(lower_limit, k):
    return lasts[lengths[k][bisect(lengths[k], lower_limit)]]
