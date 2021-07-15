def stringify(node):
    if node == None:
        return 'None'
    lst = []
    n = node
    while n.__next__ != None:
        lst.append(str(n.data))
        n = n.__next__
    lst.append(str(n.data))
    lst.append('None')
    return ' -> '.join(lst)

