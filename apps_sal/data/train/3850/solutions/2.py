def close_to_zero(t):
    return min((int(n) for n in t.split()), key=lambda n: (abs(n), n < 0), default=0)
