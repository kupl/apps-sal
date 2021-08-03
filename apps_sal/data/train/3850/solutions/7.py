def close_to_zero(t):
    return 0 if not t else int(min(sorted(t.split(), reverse=True), key=lambda x: abs(int(x))))
