def stringify(list):
    return 'None' if list == None else str(list.data) + ' -> ' + stringify(list.next)
