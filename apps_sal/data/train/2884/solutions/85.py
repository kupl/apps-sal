def stringify(node):
    if not node:
        return 'None'
    return " -> ".join([x for x in rec_stringify(node)])
    
def rec_stringify(node):
    if not node.__next__:
        return [ str(node.data), 'None']
    else:
        return [ str(node.data) ] + rec_stringify(node.__next__)

