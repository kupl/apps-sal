def stringify(node):
    n = 'None'
    if node:
        n, r = node.__next__, f"{node.data} -> "
        while n:
            r += f"{n.data} -> "
            n = n.__next__
        r += "None"
    else:
        r = n
    return r
