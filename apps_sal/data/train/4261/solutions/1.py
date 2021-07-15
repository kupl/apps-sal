def robot_walk(a):
    return any(x <= y for x,y in zip(a[1:], a[3:]))
