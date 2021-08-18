def balanced_num(numbers):
    args = []
    string_n = str(numbers)
    for i in string_n:
        args.append(int(i))
    last_index = len(args) - 1
    if len(args) % 2 == 0:
        first_index = last_index // 2
        second_index = last_index // 2 + 1
        if sum(args[0:first_index]) == sum(args[second_index + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        index = last_index // 2
        if sum(args[0:index]) == sum(args[index + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
