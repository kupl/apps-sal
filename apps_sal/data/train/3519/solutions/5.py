def duplicate_elements(m, n):
    return any(map(set(n).__contains__, m))
