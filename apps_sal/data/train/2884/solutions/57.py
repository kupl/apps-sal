def stringify(node):
    if node is not None:
        return str(node.data) + " -> " + stringify(node.next)
    else:
        return "None"
