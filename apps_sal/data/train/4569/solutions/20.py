def next_item(xs, item):
    l = []
    for i in xs:
        l.append(i)
        if item in l and len(l) == l.index(item) + 2:
            break
    return None if (item not in l or l[-1] == item) else l[l.index(item) + 1]
