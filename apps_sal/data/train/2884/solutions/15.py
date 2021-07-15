def stringify(node):
    my_str = ""
    while node:
        my_str += str(node.data) + " -> "
        node = node.next
    
    my_str += "None"
    return my_str
