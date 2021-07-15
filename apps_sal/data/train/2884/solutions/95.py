def stringify(node):
    res = ""
    while not node == None:
        res += str(node.data) + " -> "
        node = node.next
        
    res += "None"
    return res
