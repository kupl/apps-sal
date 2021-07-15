def stringify(node):
    p = node
    seq = []
    while p:
        seq.append(str(p.data))
        p = p.next
    seq.append('None')
    return ' -> '.join(seq)
