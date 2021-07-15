
def stringify(node):
    list = []
    f = node
    while f is not None:
        list.append(str(f.data))
        f = f.next
    list.append("None")
    return ' -> '.join(list)
