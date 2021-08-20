def split_by_value(k, elements):
    l = []
    elem2 = elements.copy()
    for i in elements:
        if i < k:
            l.append(i)
            elem2.remove(i)
    return l + elem2
