def same(a1, a2):
    return sorted(map(sorted, a1)) == sorted(map(sorted, a2))
