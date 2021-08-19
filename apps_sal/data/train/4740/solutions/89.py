def row_sum_odd_numbers(n):
    if n == 1:
        return 1
    startingdigit = (n - 1) * n + 1
    tot = startingdigit
    for i in range(1, n):
        startingdigit += 2
        tot += startingdigit
    return tot
