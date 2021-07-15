def sum_digits(number):
    summ = 0
    number = str(number)
    for num in number:
        if num.isdigit():
            summ += int(num)
        else:
            pass
    return summ
