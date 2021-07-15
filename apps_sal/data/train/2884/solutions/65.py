def stringify(node):
    elems = []
    cur_node = node
    while cur_node != None:
        elems.append(cur_node.data)
        cur_node = cur_node.next
    if elems == []:
        return 'None'
    return ' -> '.join(str(x) for x in elems) + ' -> ' +'None'
