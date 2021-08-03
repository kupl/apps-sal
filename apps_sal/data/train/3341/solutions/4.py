def pop_shift(s):
    i = len(s) // 2
    return [s[-1:-i - 1:-1], s[:i], s[i:i + len(s) % 2]]
