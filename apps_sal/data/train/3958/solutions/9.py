def custom_fib(signature, indexes, n):
    if n < len(signature):
        return signature[n]
    return custom_fib(signature[1:] + [sum(map(signature.__getitem__, indexes))], indexes, n - 1)
