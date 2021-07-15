def stringify(node):
    s = ''
    while node:
        s += str(node.data)
        node = node.next
        s += ' -> '
    return s + 'None'
