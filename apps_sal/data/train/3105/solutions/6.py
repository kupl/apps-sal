def count_sheep(n):
    if n == 1:
        return "1 sheep..."
    else:
        return count_sheep(n - 1) + "{} sheep...".format(n)
