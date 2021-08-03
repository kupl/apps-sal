def halving_sum(number):

    n = number

    while number != 1:
        number = number // 2
        n += number

    return n
