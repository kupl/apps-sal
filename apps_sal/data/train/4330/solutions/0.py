def shortest_arrang(n):
    # For odd n, we can always construct n with 2 consecutive integers.
    if n % 2 == 1:
        return [n//2 + 1, n//2]

    # For even n, n is the sum of either an odd number or even number of
    # consecutive positive integers. Moreover, this property is exclusive.

    for i in range(3, n // 2):
        if i % 2 == 1 and n % i == 0:
        # For odd i, if n / i is an integer, then the sequence, which has
        # odd length, is centered around n / i.
            return list(range(n//i + i//2, n//i - i//2 - 1, -1))
        elif i % 2 == 0 and n % i == i // 2:
        # For even i, if the remainder of n / i is 1/2, then the sequence
        # (even length) is centered around n / i.
            return list(range(n//i + i//2, n//i - i//2, -1))

    # If none of the above are satisfied, then n is a power of 2 and we cannot
    # write it as the sum of two consecutive integers.
    return [-1]

