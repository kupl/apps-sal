def truncate_string(s, n):
    if n >= len(s):
        return s
    elif n <= 3:
        return s[:n] + '...'
    return s[:n - 3] + '...'
