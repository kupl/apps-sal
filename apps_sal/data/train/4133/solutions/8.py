def shortest_time(n, m, speeds):
    if n == 1:
        return 0
    else:
        move, open, close, walk = speeds
        elevator = abs(n - m) * move + open + close + move * (n - 1) + open
        walking = walk * (n - 1)
    return min(elevator, walking)
