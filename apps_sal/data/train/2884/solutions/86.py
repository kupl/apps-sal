def stringify(node):
    if node == None: return 'None'
    res = ''
    while node.next != None:
        res += '{} -> '.format(node.data)
        node = node.next
    return res + str(node.data)+' -> None'
