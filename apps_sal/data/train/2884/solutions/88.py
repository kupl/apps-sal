def stringify(node):
    string = ""
    
    if node == None:
        return "None"
    else:
        n = node.next
        string = string + str(node.data) + " -> " + stringify(node.next)
        return string
