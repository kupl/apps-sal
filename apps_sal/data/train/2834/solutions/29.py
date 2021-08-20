def symmetric_point(p, q):
    distance_to_p_x = p[0] - q[0]
    distance_to_p_y = p[1] - q[1]
    return [q[0] - distance_to_p_x, q[1] - distance_to_p_y]
