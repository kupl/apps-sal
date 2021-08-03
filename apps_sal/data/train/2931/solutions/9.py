def count_cows(n):
    if not isinstance(n, int):
        return None
    cows = [1]
    old_cows = 0
    for _ in range(n):
        cows = [old_cows] + cows
        if len(cows) >= 3:
            old_cows += cows.pop()
    return sum(cows) + old_cows
