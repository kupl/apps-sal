def stringify(node):
    r = []
    while node != None:
        node = (r.append(str(node.data)), node.next)[1]
    return " -> ".join(r + ["None"])
