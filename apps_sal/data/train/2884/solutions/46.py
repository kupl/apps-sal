def stringify(node):
    list = []

    while node:
        list.append(str(node.data))
        node = node.next

    list.append('None')

    return " -> ".join(list)
