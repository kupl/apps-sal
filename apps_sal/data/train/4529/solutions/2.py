def truncate_string(str, n):
    if len(str) <= n:
        return str
    if n <= 3:
        return str[0:n] + "..."
    else:
        return str[:n - 3] + "..."
