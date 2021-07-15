def stringify(node):
    lst = []
    while node:
        lst+=[str(node.data)]
        lst+=[' -> ']
        node = node.next
    lst+=['None']
    return ''.join(lst)
