def stringify(node):
    res = []
    curr = node
    while curr:
        res.append(str(curr.data))
        curr = curr.next
    res.append('None')
    return ' -> '.join(res)
