def balanced_num(number):
    num_length = len(str(number))
    if num_length <= 2:
        return 'Balanced'
    center = num_length // 2
    num_str = str(number)
    left = 0
    if num_length % 2 == 1:
        left = sum(map(int, num_str[:center]))
    else:
        left = sum(map(int, num_str[:center - 1]))
    right = sum(map(int, num_str[center + 1:]))
    if left == right:
        return 'Balanced'
    return 'Not Balanced'
