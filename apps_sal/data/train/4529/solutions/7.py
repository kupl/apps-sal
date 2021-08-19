def truncate_string(str, n):
    return str if n >= len(str) else str[:n - 3 if n > 3 else n] + '...'
