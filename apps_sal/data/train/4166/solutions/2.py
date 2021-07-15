def solve(p):
    result = 0
    for i in range(1, int(p ** 0.5) + 1):
        if (p - 1) % i:
            continue
        if pow(10, i, p) == 1:
            result = i
            break
        j = (p - 1) // i
        if pow(10, j, p) == 1:
            result = j
    if pow(10, result // 2, p) == p - 1:
        return f'{result // 2}-altsum'
    else:
        return f'{result}-sum'
