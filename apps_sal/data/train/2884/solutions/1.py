def stringify(ll):
    r = []
    while ll:
        (r, ll) = (r + [str(ll.data)], ll.next)
    return ' -> '.join(r + ['None'])
