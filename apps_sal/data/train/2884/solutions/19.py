def stringify(node):
    if node is None:
        return 'None'
    itr = node
    llstr = ''
    while itr:
        if itr.next:
            llstr += str(itr.data) + ' -> '
        else:
            llstr += str(itr.data) + ' -> None'
        itr = itr.next
    return llstr
