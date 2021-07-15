def shortest_time(n, m, speeds):
    a, b, c, d = speeds
    elevator = (abs(m - n) + n - 1) * a + b * 2 + c
    walk = (n - 1) * d
    return min(elevator, walk)
