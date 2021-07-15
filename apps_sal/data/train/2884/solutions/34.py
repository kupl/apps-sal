def stringify(node):
    s = []
    while node:
        s.append(node.data)
        node = node.next
    s.append(None)
    return ' -> '.join(list(map(str, s)))
