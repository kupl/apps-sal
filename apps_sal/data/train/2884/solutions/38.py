def stringify(node):
    return 'None' if node is None else f"{node.data} -> {stringify(node.next)}"
