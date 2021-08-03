def stringify(node):
    if node == None:
        return 'None'
    return '{} -> {}'.format(node.data, stringify(node.__next__))
