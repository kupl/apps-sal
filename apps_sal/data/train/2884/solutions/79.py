def stringify(node):
    """Code borrowed"""

    result = ''

    while node:
        result += str(node.data) + ' -> '
        node = node.next

    return result + 'None'
