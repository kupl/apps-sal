def nth_even(n):
    if n <= 1:
        return 0
    elif n == 2:
        return n
    else:
        return n * 2 - 2
