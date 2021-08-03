def f(n):
    if isinstance(n, int):
        if n > 0:
            sum = 0
            for i in range(0, n + 1):
                sum = sum + i
            return sum
    return None
