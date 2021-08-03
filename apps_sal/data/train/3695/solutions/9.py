def repeat_adjacent(string):
    check = ''
    big_group = []
    for i in range(1, len(string) - 1):
        if (string[i - 1] == string[i] or string[i] == string[i + 1]):
            check += string[i]
        else:
            if len(set(check)) > 1:
                big_group.append(check)
            check = ''
    if len(set(check)) > 1:
        big_group.append(check)
    return len(big_group)
