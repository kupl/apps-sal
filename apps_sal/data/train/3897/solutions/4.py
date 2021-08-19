def solve(n, k):
    second_half = k >= n // 2
    return (-1) ** second_half * 2 * k + second_half * (n * 2 - 3) + 1
