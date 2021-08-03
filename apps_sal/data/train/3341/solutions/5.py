def pop_shift(s):
    i, j = divmod(len(s), 2)
    return [s[i + j:][::-1], s[:i], s[i:i + j]]
