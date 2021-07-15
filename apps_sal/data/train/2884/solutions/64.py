def stringify(node):
    return f"None" if node is None else f"{node.data} -> {stringify(node.next)}"

