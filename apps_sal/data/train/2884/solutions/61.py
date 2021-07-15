def stringify(node):
    if node == None:
        return 'None'
    ret = ''
    while node.data != None:
        ret += str(node.data) + ' -> '
        if not node.__next__:
            ret += 'None'
            break
        node = node.__next__
    return ret

