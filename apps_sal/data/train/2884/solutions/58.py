def stringify(node):
    if node == None:
        return 'None'
    elif node.next == None:
        return f"{node.data} -> None"
    else:
        return f"{node.data} -> {stringify(node.next)}"
