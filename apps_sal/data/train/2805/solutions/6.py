def productFib(prod):
    fib1, fib2 = 0, 1
    while prod > fib1*fib2:
        fib2, fib1 = fib1 + fib2, fib2
    return [fib1, fib2, prod == fib1*fib2]

