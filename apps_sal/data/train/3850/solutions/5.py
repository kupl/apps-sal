def close_to_zero(t):
    t = [int(x) for x in t.split()]
    return min(t or [0], key=lambda t: (abs(t), -t))
