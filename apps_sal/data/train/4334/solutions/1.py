def skiponacci(n):
    fib = [1, 1][:n]
    for _ in range(n - 2):
        fib.append(sum(fib[-2:]))
    return " ".join(str(n) if i % 2 else "skip" for i, n in enumerate(fib, 1))
