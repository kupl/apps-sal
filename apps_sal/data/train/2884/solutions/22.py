def stringify(node):

    if node is None:
        return 'None'

    n = node
    l = []

    while(True):
        l.append(str(n.data))
        if n.next is None:
            break
        else:
            n = n.next

    l.append('None')

    return " -> ".join(l)
