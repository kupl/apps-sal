def sum_digits(number):
    bruh = 0
    for i in str(abs(number)):
        bruh += int(i)
    return bruh
