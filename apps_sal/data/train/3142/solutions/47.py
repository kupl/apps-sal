def seven_ate9(str_):
    str_list = list(str_)
    new_list = []
    new_list.append(str_list[0])
    for i in range(1, len(str_list) - 1):
        if str_list[i] == '9':
            if str_list[i + 1] == '7' and str_list[i - 1] == '7':
                continue
            else:
                new_list.append(str_list[i])
        if str_list[i] != '9':
            new_list.append(str_list[i])
    new_list.append(str_list[-1])
    return ''.join(new_list)
