from collections import Counter
from string import ascii_letters, digits


def blocks(s):
    cnt = Counter(sorted(s, key=(ascii_letters + digits).index))
    res = []
    while cnt:
        res.append(''.join(cnt.keys()))
        cnt = {k: v - 1 for (k, v) in cnt.items() if v > 1}
    return '-'.join(res)
