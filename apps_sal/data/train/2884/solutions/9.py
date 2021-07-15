def stringify(node):
    if not node:
        return 'None'
    return '{} -> {}'.format(node.data, stringify(node.next))
