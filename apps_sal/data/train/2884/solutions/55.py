def stringify(node):
    if not node:
        return 'None'
    list = [str(node.data)]
    curr = node
    while curr != None:
        curr = curr.next
        list.append(str(curr.data) if curr else 'None')
    return ' -> '.join(list)
