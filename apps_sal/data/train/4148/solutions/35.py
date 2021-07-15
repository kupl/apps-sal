def sum_digits(number):
    y = 0
    for x in str(number):
        if x == "-":
            pass
        else:
            y += int(x)
    return y
