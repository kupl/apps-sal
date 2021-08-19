def remove_char(s):
    s_list = []
    for x in s:
        s_list.append(x)
    return ''.join(s_list[1:len(s) - 1])
