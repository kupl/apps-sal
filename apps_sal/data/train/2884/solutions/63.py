def stringify(node):
    if node==None:
        return "None"
    return f"{node.data} -> {stringify(node.next)}"

