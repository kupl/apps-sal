def robot_walk(a):
    return any((i > 2 and a[i - 2] <= p for (i, p) in enumerate(a)))
