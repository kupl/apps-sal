def find_longest(arr):
    l = list(map(str, arr))
    return int(sorted(l, key=lambda x: (len(str(x)), -l.index(x)))[-1])
