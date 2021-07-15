def stringify(node):
    if node == None:
        return str('None')
    return str(node.data) + " -> " + stringify(node.next)
