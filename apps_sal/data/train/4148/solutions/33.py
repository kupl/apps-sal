def sum_digits(number):
    asum = 0
    for val in str(number):
        if val != '-':
            print(val)
            asum += int(val)
    return asum
