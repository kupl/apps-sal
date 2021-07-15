def invert(lst):
    new_list = lst
    result_list = []
    for number in new_list:
        if number > 0:
            result_list.append(number * -1)
        else:
            result_list.append(number - number * 2)
    return result_list
