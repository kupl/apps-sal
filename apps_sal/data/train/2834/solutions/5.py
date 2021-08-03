def symmetric_point(p, q):
    # your code here
    return [a * 2 - b for a, b in zip(q, p)]
