def custom_fib(signature, indexes, n):
    for _ in range(n):
        signature = signature[1:] + [sum(signature[i] for i in indexes)]
    return signature[0]
