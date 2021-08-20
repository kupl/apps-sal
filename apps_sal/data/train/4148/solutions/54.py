def sum_digits(number):
    num = str(number)
    num = num.lstrip('-')
    result = 0
    for i in num:
        result += int(i)
    return result
