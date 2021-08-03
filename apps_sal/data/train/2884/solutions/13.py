def stringify(node):
    if not node:
        return 'None'
    if node.__next__:
        return f'{node.data} -> {stringify(node.next)}'
    else:
        return f'{node.data} -> None'
