def min_value(digits):
    list_1 = []
    for i in digits:
        list_1.append(i)
    final_list = list(set(list_1))
    final_list.sort()
    print(final_list)
    str_nums = [str(x) for x in final_list]
    print(str_nums)
    lowest_number = ''.join(str_nums)
    lowest_number = int(lowest_number)
    return lowest_number
