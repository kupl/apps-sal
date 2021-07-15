def max_multiple(divisor, bound):
    if bound % divisor == 0:
        return bound
    else:
        x = int(bound/divisor)
        return divisor * x

