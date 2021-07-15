from collections import Counter


def solve(files):
    count = Counter(f.rsplit(".")[-1] for f in files)
    m = max(count.values(), default=0)
    return sorted(f".{ext}" for ext, c in count.items() if c == m)
