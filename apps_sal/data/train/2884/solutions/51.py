def stringify(node):
    if node:
        if not node.next:
            return f'{node.data} -> None'
        return f'{node.data} -> {stringify(node.next)}'
    else:
        return 'None'
