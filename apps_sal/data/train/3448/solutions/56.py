def f(n):
    if isinstance(n, str):
        return None
    if isinstance(n, float):
        return None
    if n <= 0:
        return None
    count = 0
    for i in range(n + 1):
        count += i

    return count
