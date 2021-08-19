def shortest_time(a):
    return a.sort() or a[0] + a[1] + min(2 * a[1], a[0] + a[2]) + a[3]
