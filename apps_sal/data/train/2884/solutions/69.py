def stringify(node):
    currentNode = node
    res = ''
    while currentNode is not None:
        res += f'{currentNode.data} -> '
        currentNode = currentNode.next
    if currentNode is None:
        res += 'None'
        
    return res
