def halving_sum(n):

    x = n

    while n != 1:
        x += n // 2
        n //= 2

    return x
