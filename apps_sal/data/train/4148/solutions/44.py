def sum_digits(number):
    sumnumbers=0
    for numbers in str(number.__abs__()):
        sumnumbers += int(numbers)
    return sumnumbers
