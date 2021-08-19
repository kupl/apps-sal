from collections import Counter


def solve(files):
    ext = [f.split('.')[-1] for f in files]
    return sorted(('.' + i for i in set(ext) if ext.count(i) == max((ext.count(i) for i in ext))))
