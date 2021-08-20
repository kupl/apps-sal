def skiponacci(n):
    fib = [1, 1][:n]
    for _ in range(n - 2):
        fib.append(sum(fib[-2:]))
    return ' '.join(('skip' if c % 2 else str(a) for (c, a) in enumerate(fib)))
