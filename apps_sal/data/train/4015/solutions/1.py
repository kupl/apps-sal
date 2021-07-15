from collections import Counter

def paint_letterboxes(s, f):
    a = Counter("".join(map(str, range(s, f+1))))
    return [a[x] for x in "0123456789"]
