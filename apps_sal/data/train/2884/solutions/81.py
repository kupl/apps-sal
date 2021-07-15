def stringify(node):
    seq, current = [], node
    while current:
        seq.append(str(current.data))
        current = current.next
    seq.append('None')
    return ' -> '.join(seq)
