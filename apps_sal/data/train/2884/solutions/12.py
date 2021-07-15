def stringify(node):
    if node == None:
        return "None"
    return str(node.data) + " -> " + stringify(node.next)
