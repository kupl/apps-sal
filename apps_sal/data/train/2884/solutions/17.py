def recursive(node, string):
    if node is None:
        string += "None"
        return string
    string += str(node.data) + " -> "
    node = node.next
    return recursive(node, string)

def stringify(node):
    string = ""
    ans = recursive(node, string)
    return ans
