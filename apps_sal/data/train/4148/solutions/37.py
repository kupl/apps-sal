def sum_digits(number):
    if number >= 0:
        total = 0
        for i in str(number):
            total += int(i)
        return total
    else:
        total = 0
        for i in str(number)[1:]:
            total += int(i)
        return total
