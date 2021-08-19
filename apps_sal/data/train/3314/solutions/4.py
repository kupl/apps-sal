def solve(a, b):
    (li, j) = ([], 2)
    while b > 1:
        if b % j:
            j += 1
            continue
        li.append(j)
        b //= j
        if a % j:
            return 0
    return 1
