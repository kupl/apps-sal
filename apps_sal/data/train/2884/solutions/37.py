def stringify(node):
    x = []

    while True:
        try:
            x.append(str(node.data))
            node = node.next
        except:
            break
    x.append('None')
    return ' -> '.join(x)
