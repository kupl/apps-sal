def even_fib(m):
    """Returns the sum of all even numbers in a Fibonacci sequence
    up to the maximum value m (non-inclusive of m)."""

    a, b, evens_sum = 0, 1, 0

    while (a + b) < m:
        if (a + b) % 2 == 0:
            evens_sum += (a + b)

        a, b = b, (a + b)

    return evens_sum
