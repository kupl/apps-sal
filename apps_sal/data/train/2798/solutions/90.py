def to_alternating_case(a):
    lst = []
    for i in a:
        if i == i.lower():
            lst.append(i.upper())
        else:
            lst.append(i.lower())
    return ''.join(lst)
