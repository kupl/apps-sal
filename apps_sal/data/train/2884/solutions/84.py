def stringify(node):
    if not node:
        return "None"
    output = ""
    while node:
        output += str(node.data) + " -> "
        node = node.next
    output += "None"
    return output
