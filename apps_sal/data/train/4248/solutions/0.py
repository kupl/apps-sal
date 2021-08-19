from collections import Counter
import re


def solve(files):
    c = Counter((re.match('.*(\\.[^.]+)$', fn).group(1) for fn in files))
    m = max(c.values(), default=0)
    return sorted((k for k in c if c[k] == m))
