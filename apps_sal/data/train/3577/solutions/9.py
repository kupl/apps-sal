from collections import Counter


def fib_digits(n):
    first = 0
    second = 1
    for i in range(n - 1):
        update = first + second
        first = second
        second = update
    return list(reversed(sorted([(v, k) for (k, v) in Counter([int(y) for y in str(update)]).items()])))
