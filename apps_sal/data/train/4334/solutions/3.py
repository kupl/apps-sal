fib, result = [1, 1], ["1", "skip"]
for i in range(100):
    fib.append(fib[-1] + fib[-2])
    result.append("skip" if i & 1 else str(fib[-1]))


def skiponacci(n):
    return ' '.join(result[:n])
