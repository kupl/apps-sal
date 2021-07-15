def stringify(node):
    r = ''

    while node != None:
        r += f'{node.data} -> '
        node = node.next
    
    return r + 'None'
