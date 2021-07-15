def truncate_string(str,n):
    if len(str) <= n:
        return str
    if n <= 3:
        return str[:n] + '...'
    return str[:n-3] + '...'
