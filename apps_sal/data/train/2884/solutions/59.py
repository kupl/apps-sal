def stringify(node):
    if not node: return "None"
    ls = []
    while node.next != None:
        ls.append(str(node.data))
        node = node.next
    ls.append(str(node.data) +" -> None")
    return " -> ".join(ls)
