def stringify(node):
    return ''.join(str(node.data) + ' -> ' + stringify(node.next)) if node else 'None'
