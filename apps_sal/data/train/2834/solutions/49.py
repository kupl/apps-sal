def symmetric_point(p, q):
    # your code here
    x = q[0] - p[0]
    y = q[1] - p[1]
    return [q[0] + x, q[1] + y]
