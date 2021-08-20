def fib_rabbits(end, factor):
    (immatures, adults) = (1, 0)
    for month in range(end):
        (immatures, adults) = (factor * adults, adults + immatures)
    return adults
