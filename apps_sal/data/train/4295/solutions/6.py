def balanced_num(number):
    st_num = str(number)
    if number < 100:
        return 'Balanced'
    half_len = len(st_num) // 2 if len(st_num) % 2 != 0 else (len(st_num) - 1) // 2
    right_sum, left_sum = 0, 0
    for i in range(half_len):
        left_sum += int(st_num[i])
        right_sum += int(st_num[-1 - i])
    return 'Balanced' if left_sum == right_sum else 'Not Balanced'
