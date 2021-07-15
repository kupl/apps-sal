def collatz(n):
    l = [str(n)]
    while n > 1:
        n = 3 * n + 1 if n % 2 else n / 2
        l.append(str(n))
    return '->'.join(l)
