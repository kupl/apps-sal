def sum_digits(number):
    number = abs(number)
    number = str(number)
    sum_num = 0    
    for i in number:
        i = int(i)
        sum_num = sum_num + i
    return sum_num
