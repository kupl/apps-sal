def sum_digits(number):
    nr = str(number)
    total = 0
    for i in range(len(nr)):
        if nr[i].isdigit():
            total += int(nr[i])
    return total
