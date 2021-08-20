def even_fib(m):
    result = [0, 1]
    while result[-1] < m:
        result.append(sum(result[-2:]))
    return sum((num for num in result if num % 2 == 0 and num < m))
