def sum_digits(number):
    str_num = str(number)
    ret_num = 0
    for num in str_num:
        if num != '-':
            ret_num = ret_num + int(num)
    return ret_num
