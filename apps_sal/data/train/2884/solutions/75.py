def stringify(node):
    if node is None:
        return "None"
    elif node.next is None:
        return f"{node.data} -> None"
    else:
        return f"{node.data} -> {stringify(node.next)}"
