def solve(arr):
    res = []
    for w in arr:
        res.append(sum(ord(l.lower()) - 97 == i for i, l in enumerate(w)))
    return res
