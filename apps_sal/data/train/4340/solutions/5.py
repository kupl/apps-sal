def shortest_time(speed):
    speed.sort()
    [a, b, c, d] = speed
    return min(a + 3 * b + d, 2 * a + b + c + d)
