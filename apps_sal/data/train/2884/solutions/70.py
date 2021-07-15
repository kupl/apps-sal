def stringify(node):
    result = ''
    while node != None:
        result += f'{node.data} -> '
        node = node.next
    result += 'None'
    return result
