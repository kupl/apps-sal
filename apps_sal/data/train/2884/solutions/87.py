def stringify(node):
    st = ''
    while node:
        st = st + str(node.data) + ' -> '
        node = node.__next__
    st = st + 'None'
    return st
