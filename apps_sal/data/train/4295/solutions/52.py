def balanced_num(num):
    num_string = str(num)
    nums_left_str = ''
    nums_right_str = ''
    left_sum = 0
    right_sum = 0
    return_string = ''
    middle_index = 0
    middle_index = len(num_string) // 2
    if len(num_string) % 2 != 0:
        nums_left_str = num_string[:middle_index]
        nums_right_str = num_string[middle_index + 1:]
        print("it's odd")
    else:
        nums_left_str = num_string[:middle_index - 1]
        nums_right_str = num_string[middle_index + 1:]
        print("it's even")
    print('nums_left_str == ' + nums_left_str)
    print('nums_right_str == ' + nums_right_str)
    for i in range(len(nums_left_str)):
        left_sum += int(nums_left_str[i])
    for i in range(len(nums_right_str)):
        right_sum += int(nums_right_str[i])
    if right_sum == left_sum:
        return_string = 'Balanced'
    else:
        return_string = 'Not Balanced'
    return return_string
