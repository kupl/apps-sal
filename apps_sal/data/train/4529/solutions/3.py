def truncate_string(str, n):
    if n >= len(str):
        return str
    return [str[:n] + '.' * 3, str[:n - 3] + '.' * 3][n > 3]
