def solve(arr):
    negative = set([i for i in arr if i < 0])
    positive = set([i for i in arr if i > 0])
    res = None
    for i in negative:
        if i * -1 not in positive:
            res = i
    for i in positive:
        if i * -1 not in negative:
            res = i
    return res
