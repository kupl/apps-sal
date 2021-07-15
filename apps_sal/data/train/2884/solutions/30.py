def stringify(node):
    return f'{node.data} -> {stringify(node.next)}' if node else str(None)
