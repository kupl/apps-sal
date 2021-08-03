def halving_sum(n):

    number = n
    while number > 1:
        n += int(number / 2)
        number /= 2
    return n
