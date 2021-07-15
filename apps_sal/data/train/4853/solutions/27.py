def double_char(s):
    new_list = []
    for x in s:
        new_list.append(x)
        new_list.append(x)
    return ''.join(new_list)
