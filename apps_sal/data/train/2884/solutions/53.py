def stringify(node):
    if node != None:
        return f'{node.data} -> ' + stringify(node.next)
    else:
        return 'None'
