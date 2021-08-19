def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]
