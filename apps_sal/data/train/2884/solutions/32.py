def stringify(node):
    if node == None:
        return 'None'
    else:
        s = str(node.data) + ' -> '
        return s + stringify(node.next)
