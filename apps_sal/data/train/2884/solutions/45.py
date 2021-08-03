def stringify(node):
    node_str = ''
    while node:
        arrow = ' -> '
        node_str += str(node.data) + arrow
        node = node.__next__
    return node_str + 'None'
