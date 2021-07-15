def stringify(node):
    res = ''
    while node:
        res += '{} -> '.format(str(node.data))
        node = node.next
    return res + 'None'
