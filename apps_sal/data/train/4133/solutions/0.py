def shortest_time(n, m, speeds):
    lift, open, close, walk = speeds
    return min(
            # taking the elevator
            abs(m - n) * lift + open + close + (n - 1) * lift + open,
            # walking
            (n - 1) * walk
            )
