def stringify(node):
    a = []
    if not node:
        return 'None'
    while node:
        a.append(str(node.data))
        node = node.__next__
    a.append('None')
    print(a)
    return ' -> '.join(a)

