def same(a, b):
    return comp(a) == comp(b)

def comp(arr):
    return sorted(map(sorted,arr))
