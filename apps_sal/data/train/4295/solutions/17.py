def balanced_num(number):
    number = str(number)
    len_num = len(number)
    balanced = sum(map(int, number[:len_num // 2 - (len_num % 2 == 0)])) == sum(map(int, number[len_num // 2 + 1:]))
    return 'Balanced' if balanced else 'Not Balanced'
