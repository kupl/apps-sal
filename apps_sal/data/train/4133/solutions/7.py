def shortest_time(n, m, speeds):
    (a, b, c, d) = speeds
    return min(d * (n - 1), (abs(m - n) + n - 1) * a + 2 * b + c)
