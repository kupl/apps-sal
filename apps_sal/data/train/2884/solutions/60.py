def stringify(node):
    return 'None' if node is None else '%d -> %s' % (node.data, stringify(node.__next__))

