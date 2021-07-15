def stringify(node):
    try:
        emptylist = []
        while type(node.data) is int:
            emptylist.append(str(node.data))
            node = node.next
    except:
        emptylist.append('None')
        return ' -> '.join(emptylist)
