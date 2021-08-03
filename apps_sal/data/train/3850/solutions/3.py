def close_to_zero(t):
    return sorted(map(int, t.split()), key=lambda i: (abs(i), -i))[0] if t else 0
