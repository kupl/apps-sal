from bisect import bisect_left

def yoga(a, b):
    c = []
    for x in a:
        y = sum(x)
        c.append([z + y for z in sorted(x)])
    return sum(sum(len(x) - bisect_left(x, y) for y in b) for x in c)
