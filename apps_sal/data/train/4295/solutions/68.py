def balanced_num(number):
    str_n = str(number)
    len_n = len(str_n)
    mid = len_n // 2
    if len_n % 2 != 0:
        flag = sum((int(i) for i in str_n[:mid])) == sum((int(i) for i in str_n[mid + 1:]))
    else:
        flag = sum((int(i) for i in str_n[:mid - 1])) == sum((int(i) for i in str_n[mid + 1:]))
    return 'Balanced' if flag else 'Not Balanced'
