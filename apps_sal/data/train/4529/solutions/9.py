def truncate_string(s, n):
    p = s[:n - 3] if n > 3 else s[:n]
    return p + '...' if len(s) > n else s
