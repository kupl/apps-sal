def stringify(node):
    list = []
    while node:
        list.append(node.data)
        node = node.next
    list.append('None')
    return ' -> '.join(map(str, list))
