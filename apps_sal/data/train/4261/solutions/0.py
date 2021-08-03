def robot_walk(a):
    i = 3
    while(i < len(a) and a[i] < a[i - 2]):
        i += 1
    return i < len(a)
