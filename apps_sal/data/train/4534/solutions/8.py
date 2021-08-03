
def find_next_power(val, pow_):
    num, next_power_value = 1, 1
    while val > next_power_value:
        next_power_value = num ** pow_
        num += 1

    return next_power_value
