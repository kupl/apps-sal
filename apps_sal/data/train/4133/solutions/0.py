def shortest_time(n, m, speeds):
    (lift, open, close, walk) = speeds
    return min(abs(m - n) * lift + open + close + (n - 1) * lift + open, (n - 1) * walk)
