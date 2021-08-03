def stringify(node):
    if not node:
        return 'None'
    string = node.data
    node = node.next
    while node:
        string = f'{string} -> {node.data}'
        node = node.next
    return f'{string} -> {node}'
