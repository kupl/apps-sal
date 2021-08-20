def stringify(node):
    List = []
    while node and node.data != None:
        List.append(str(node.data))
        node = node.next
    List.append('None')
    return ' -> '.join(List)
