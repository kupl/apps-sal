def sum_digits(number):
    number_list = list(str(number))
    sum = 0
    print(number_list)
    for x in number_list:
        if x == '-':
            continue
        else:
            sum += int(x)
    return sum
