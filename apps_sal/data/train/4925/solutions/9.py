def collatz(n):
    seq = [str(n)]
    while n > 1:
        n = 3 * n + 1 if n % 2 else n // 2
        seq.append(str(n))
    return '->'.join(seq)
