def f(n):
    if not isinstance(n, int):
        return
    result = 0
    for x in range(n + 1):
        result += x
    return result if result > 0 else None
