def stringify(node):
    head = node
    curr = head
    strList = []
    while (curr != None):
        strList.append(curr.data)
        curr = curr.next
    strList.append(None)
    
    return ' -> '.join(str(x) for x in strList)
