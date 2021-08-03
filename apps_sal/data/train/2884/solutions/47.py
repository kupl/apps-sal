def stringify(node):
    if node == None:
        return "None"
    string = str(node.data)
    node = node.next
    while node != None:
        string = string + " -> " + str(node.data)
        node = node.next
    return (string + " -> None")
