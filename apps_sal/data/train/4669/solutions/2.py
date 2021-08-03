def beggars(values, n):
    if n == 0:
        return []
    i = 0
    take = []
    for x in range(n):
        take.append(0)
    for val in values:
        take[i % n] = take[i % n] + val
        i = i + 1
    return take
