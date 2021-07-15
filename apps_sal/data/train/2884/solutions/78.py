def stringify(node):
    ret = ""
    while node:
      ret += str(node.data) +  " -> "
      node = node.next
    return ret + "None"
