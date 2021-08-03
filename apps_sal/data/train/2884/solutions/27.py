def stringify(node):
    new = []
    node = node
    while node is not None:
        new.append(str(node.data))
        node = node.next
    else:
        new.append('None')
    return ' -> '.join(new)
