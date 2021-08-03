def tidyNumber(n):
    str_num = str(n)
    digit_list = [d for d in str_num]
    return digit_list == sorted(digit_list)
