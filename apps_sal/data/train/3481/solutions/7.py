from collections import Counter
from itertools import groupby


def get_char_count(s):
    cnt = Counter(c for c in s.lower() if c.isalnum()).most_common()
    return {k: sorted(map(lambda x: x[0], vs)) for k, vs in groupby(cnt, key=lambda x: x[1])}
