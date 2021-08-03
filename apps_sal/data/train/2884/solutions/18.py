def stringify(node):
    if node is None:
        return 'None'

    data = node.data
    list = []
    current_node = node

    while current_node is not None:
        list.append(str(current_node.data))
        current_node = current_node.__next__

    if current_node is None:
        list.append("None")

    return " -> ".join(list)
