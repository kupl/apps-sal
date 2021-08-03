def nth_even(n):
    #     Q = [x for x in range(n*8) if x % 2 == 0]
    #     return Q[n-1]
    if n == 1:
        return 0
    elif n >= 2:
        return n + (n - 2)
