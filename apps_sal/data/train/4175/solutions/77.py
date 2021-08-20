def repeater(string, n):
    str_list = []
    for x in range(n):
        str_list.append(string)
    return ''.join(str_list)
