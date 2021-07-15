def stringify(node):
    string_list = ""
    current = node
    while current:
        string_list += str(current.data) + " -> "
        current = current.next
    string_list += "None"
    return string_list
