from functools import reduce, lru_cache


def calc(k, n, m, x):
    n_of_eq_var = sum(fib(i) for i in range(1, n - 4)) + 2
    got_on_2nd = int(
        (m - k * n_of_eq_var) / sum(fib(i) for i in range(1, n - 3))
    )

    return reduce(
        lambda result, i: result + fib(i, k, got_on_2nd), range(1, x - 1), k
    )


@lru_cache(None)
def fib(n, fib_1=1, fib_2=1):
    for _ in range(n - 2):
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return fib_2 if n > 1 else fib_1
