def stringify(node):
    string = ''
    while node:
        string += str(node.data)
        string += ' -> '
        node = node.next
    string += 'None'
    return string
