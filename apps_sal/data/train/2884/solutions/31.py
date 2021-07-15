def stringify(node):
    a = ''
    if node == None:
        return 'None'
    else:
        node_data = str(node.data)
        #a = node_data + ' -> '
        #a += stringify(node.next)
        return node_data + ' -> ' + stringify(node.__next__)
        

