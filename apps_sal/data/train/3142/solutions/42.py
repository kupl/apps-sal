def seven_ate9(str_):
    lst = list(str_)
    cursor = 1
    while cursor < len(lst) - 1:
        if lst[cursor] == '9' and lst[cursor - 1] == '7' and (lst[cursor + 1] == '7'):
            lst[cursor] = None
        cursor += 1
    return ''.join([item for item in lst if item])
