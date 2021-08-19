def symmetric_point(p, q):
    # your code here
    return [
        q[0] + (q[0] - p[0]),   # x
        q[1] + (q[1] - p[1]),   # y
    ]
