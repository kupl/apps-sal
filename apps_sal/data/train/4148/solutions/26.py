def sum_digits(number):
    digits = list(map(str, str(number)))
    digits = [int(x) for x in digits if x.isdigit()]
    return sum(digits)

