def shortest_time(n, m, speeds):
    (a, b, c, d) = speeds
    return min((n - 1) * d, a * (abs(m - n) + n - 1) + 2 * b + c)
