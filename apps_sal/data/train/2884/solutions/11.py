def stringify(list):
    return str(list.data) + ' -> ' + stringify(list.next) if list else 'None'
