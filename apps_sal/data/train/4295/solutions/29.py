def balanced_num(number):
    string_number = str(number)
    if len(string_number) <= 2:
        return 'Balanced'
    list_number = [int(i) for i in list(str(string_number))]
    if len(string_number) == 3:
        if list_number[0] == list_number[-1]:
            return 'Balanced'
        else:
            return 'Not Balanced'
    if len(list_number) % 2 == 0:
        middle_number = int(len(list_number) // 2)
        if sum(list_number[:middle_number - 1]) == sum(list_number[middle_number + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        middle_number = int(len(list_number) // 2 + 1)
        if sum(list_number[:middle_number - 1]) == sum(list_number[middle_number:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
