def stringify(node):
    if not node:
        return "None"
    if not node.__next__:
        return f"{node.data} -> {None}"
    return f"{node.data} -> {stringify(node.next)}"


