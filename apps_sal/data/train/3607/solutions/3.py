def valid(num, power):
    return num == sum((int(x) ** power for x in str(num)))


def eq_sum_powdig(hMax, exp):
    return [x for x in range(2, hMax + 1) if valid(x, exp)]
