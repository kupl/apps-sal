def get_sum_of_digits(num):
    sum = 0
    str_num = str(num)
    for x in str_num:
        sum += int(x)
    return sum
