def list_squared(m, n):
    squared_divisors = []
    for i in range(m, n + 1):
        if i == 1:
            div = [1]
        else:
            div = [j for j in range(1, int(i**0.5) + 1) if i % j == 0 for j in (j, i // j) if i / j != j]
        tot = sum(k * k for k in div)**0.5
        if tot == int(tot):
            squared_divisors.append([i, int(tot**2)])
    return squared_divisors
