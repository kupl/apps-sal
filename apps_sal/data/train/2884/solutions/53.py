def stringify(node):
    # base case
    if node != None:
        return f'{node.data} -> ' + stringify(node.next)
    else:
        return 'None'
