def sum_digits(number):

    num_str = str(abs(number))
    s = 0

    for i in num_str:
        s += int(i)
    return s
