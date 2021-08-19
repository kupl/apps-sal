def nth_even(n):
    array = list(range(0, n * 2, 2))
    if array[n - 1] % 2 == 0:
        return array[n - 1]
