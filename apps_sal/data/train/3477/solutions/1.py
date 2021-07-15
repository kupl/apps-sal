def sort_string(s, ordering):
    dct = {c:-i for i,c in enumerate(reversed(ordering))}
    return ''.join(sorted(s,key=lambda c:dct.get(c,1)))
