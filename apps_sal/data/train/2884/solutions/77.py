def stringify(node):
    if node is None:
        return 'None'
    output = str(node.data) + ' -> '
    while node.next != None:
        node = node.next
        output += str(node.data) + ' -> '
    output += 'None'
    return output
