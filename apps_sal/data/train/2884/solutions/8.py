def stringify(node):
    return 'None' if not node else f'{str(node.data)} -> ' + stringify(node.__next__)
