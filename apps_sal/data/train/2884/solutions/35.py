def stringify(node):
    s = ""
    while node:
        s += f"{node.data} -> "
        node = node.next
    s += "None"
    return s
