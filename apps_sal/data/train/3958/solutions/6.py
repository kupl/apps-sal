def custom_fib(signature, indexes, n):
    values, l = list(signature), len(signature)
    while len(values) <= n:
        values.append(sum(values[-l:][i] for i in indexes))
    return values[n]
