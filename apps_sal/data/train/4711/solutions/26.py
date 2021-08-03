def zeros(n):

    if n / 5 <= 0:
        return 0
    else:
        n //= 5
        return n + zeros(n)
