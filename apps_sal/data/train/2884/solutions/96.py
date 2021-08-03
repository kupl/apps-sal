def stringify(node):
    to_print = ''
    while node != None:
        to_print += str(node.data) + ' -> '
        node = node.__next__
    return to_print + 'None'
