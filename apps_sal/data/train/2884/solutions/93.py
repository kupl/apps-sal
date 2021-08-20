def stringify(node):
    ret = ''
    try:
        while node.data != None:
            ret += str(node.data) + ' -> '
            node = node.next
    except:
        ret += 'None'
    return ret
