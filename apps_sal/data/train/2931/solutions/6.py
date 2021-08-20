def count_cows(n):
    if not isinstance(n, int):
        return None
    cows = [0, 0, 0, 1]
    for _ in range(n):
        cows = [cows[0] + cows[1], cows[2], cows[3], cows[0] + cows[1]]
    return sum(cows)
