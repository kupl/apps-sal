from collections import defaultdict


def group_cities(l):
    def make_key(s):
        return min(s[-i:] + s[:-i] for i in range(len(s)))
    d = defaultdict(list)
    for item in sorted(set(l)):
        d[make_key(item.lower())].append(item)
    return sorted(d.values(), key=len, reverse=True)
