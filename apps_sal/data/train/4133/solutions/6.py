def shortest_time(n,m,speeds):
    b = (n - 1 + max(m, n) - min(m, n)) * speeds[0] + speeds[2] + speeds[1]*2
    a = speeds[-1] * (n-1)
    return b if a > b else a
