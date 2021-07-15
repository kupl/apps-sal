def find_digit(num, nth):
    str_num = str(num)
    if nth < 1:
        return -1
    if nth > len(str_num):
        return 0
    return int(str_num[::-1][nth - 1])
