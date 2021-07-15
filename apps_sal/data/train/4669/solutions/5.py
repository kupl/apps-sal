def beggars(values, n):
    return [sum(values[k::n]) for k in range(n)]
