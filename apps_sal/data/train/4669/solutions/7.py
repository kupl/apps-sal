def beggars(values, n):
    return [sum(values[i] for i in range(j, len(values), n)) for j in range(n)]
