def stringify(node):
    s = []
    while node:
        s.append(str(node.data))
        node = node.next
    s.append('None')
    return ' -> '.join(s)
