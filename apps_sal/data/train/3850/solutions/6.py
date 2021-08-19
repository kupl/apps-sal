def close_to_zero(t):
    return min(map(int, t.split()), key=lambda n: (abs(n), -n), default=0)
