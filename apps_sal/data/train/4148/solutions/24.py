def sum_digits(number):
    sum = 0
    for char in str(number):
        if char == '-':
            continue
        else:
            sum = sum + eval(char)
    return sum
