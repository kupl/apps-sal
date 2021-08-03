def beggars(values: list, n: int):
    if n < 1:
        return []

    beggars = [0] * n
    for i, v in enumerate(values):
        beggars[i % n] += v

    return beggars
