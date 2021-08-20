def hotpo(n):
    res = 0
    number = n
    if number == 1:
        return res
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        res += 1
    return res
