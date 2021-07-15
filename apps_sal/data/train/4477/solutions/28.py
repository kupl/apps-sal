def reverse_number(n):
    str_num = str(abs(n))[::-1]
    return -1 * int(str_num) if n < 0 else int(str_num)
