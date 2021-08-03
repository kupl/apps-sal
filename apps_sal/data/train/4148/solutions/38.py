def sum_digits(num):
    return sum([int(i) for i in str(num) if i.isdigit()])
