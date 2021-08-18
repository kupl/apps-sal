def stringify(node):
    a = ''
    if node == None:
        return 'None'
    else:
        node_data = str(node.data)
        return node_data + ' -> ' + stringify(node.__next__)
