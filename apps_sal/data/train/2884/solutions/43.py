def stringify(node, s=''):
    if not node:
        s = s + 'None'
        return s
    else:
        s = s + str(node.data) + ' -> '
        return stringify(node.next, s)
