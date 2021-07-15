def nb_dig(n, d):
    integers = [str(integer ** 2) for integer in range(n + 1)]
    return sum([digits.count(str(d)) for digits in integers])
