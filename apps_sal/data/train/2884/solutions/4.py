def stringify(list):
    return 'None' if list is None else str(list.data) + ' -> ' + stringify(list.next)
