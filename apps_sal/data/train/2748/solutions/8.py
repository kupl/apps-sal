def namelist(names):
    names_lst = []
    for i in range(len(names)):
        names_lst.append(names[i]['name'])
    names_str = ''
    for i in range(len(names_lst)):
        names_str += names_lst[i]
        if i < len(names_lst) - 2:
            names_str += ', '
        elif i == len(names_lst) - 2:
            names_str += ' & '
    return names_str
