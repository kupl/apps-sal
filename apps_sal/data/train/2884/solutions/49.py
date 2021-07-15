def stringify(node):
    if node == None: return 'None'
    i = node
    t = ''
    while i.next != None:
        t += str(i.data) + ' -> '
        i = i.next
    t += str(i.data) + ' -> None'
    return t
