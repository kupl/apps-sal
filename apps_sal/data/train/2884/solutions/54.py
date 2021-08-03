def stringify(node):
    if node is None:
        return 'None'

    result = ''
    while node.__next__ is not None:
        result += str(node.data)
        result += ' -> '
        node = node.__next__
    result += str(node.data)
    result += ' -> None'

    return result
