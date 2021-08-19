def stringify(node):
    if node == None:
        return 'None'
    n = node
    r = ''
    while n.next != None:
        r = r + str(n.data) + ' -> '
        n = n.next
    return r + str(n.data) + ' -> None'
