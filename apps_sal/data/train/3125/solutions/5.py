def solve(n):
    X = 1e9
    for i in range(1, int(n**(1 / 2)) + 1):
        if n % i == 0:
            a = i
            b = n // i
            if b - a != 0 and (b - a) % 2 == 0:
                X = min(X, (b - a) // 2)
    return(X * X if X != 1e9 else -1)
