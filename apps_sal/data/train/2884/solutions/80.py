def stringify(node):
    curr = node
    res = []
    while curr != None:
        res.append(curr.data)
        curr = curr.next
    res.append(None)
    return ' -> '.join((str(x) for x in res))
