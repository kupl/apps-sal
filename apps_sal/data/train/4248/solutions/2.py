import os
from collections import Counter


def solve(files):
    c = Counter((os.path.splitext(f)[-1] for f in files))
    m = max(c.values(), default=0)
    return [x for x in sorted(c) if c[x] == m]
