def find_pattern():
    fib = [1, 1, 2]
    while fib[-2:] != [1, 1]:
        fib.append((fib[-2] + fib[-1]) % 10)
    return fib[:-2]


pattern = find_pattern()


def last_fib_digit(n):
    return pattern[(n - 1) % len(pattern)]
