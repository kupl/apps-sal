def solve(arr):
    pos = set([x for x in arr if x > 0])
    neg = set([abs(x) for x in list([x for x in arr if x < 0])])
    if pos.issubset(neg):
        return (neg - pos).pop() * (-1)
    else:
        return (pos - neg).pop()
