def symmetric_point(p, q):
    (delta_x, delta_y) = (abs(q[0] - p[0]), abs(q[1] - p[1]))
    return [q[0] + delta_x if p[0] < q[0] else q[0] - delta_x, q[1] + delta_y if p[1] < q[1] else q[1] - delta_y]
