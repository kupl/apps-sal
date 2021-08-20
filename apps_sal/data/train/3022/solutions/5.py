def two_highest(arg1):
    if type(arg1) is list:
        new_list = sorted(list(set(arg1)))
        new_list.reverse()
        return new_list[0:2]
    else:
        return False
