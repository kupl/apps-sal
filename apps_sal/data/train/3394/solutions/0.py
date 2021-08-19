def collatz(n):
    step = 1
    while n != 1:
        n = [n // 2, n * 3 + 1][n % 2]
        step += 1
    return step
