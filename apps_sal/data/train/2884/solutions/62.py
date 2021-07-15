def stringify(node):
    if node is None:
        return 'None'
    res = []
    while True:
        if node.__next__ is None:
            res.append(str(node.data))
            res.append('None')
            break
        res.append(str(node.data))
        node = node.__next__
    return ' -> '.join(res)

