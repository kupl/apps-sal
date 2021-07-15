def next_item(xs, item):
    c = 0
    l = []
    for x in iter(xs):
        if x == item:
            l.append(x)
            c += 1
        elif c == 1:
            l.append(x)
            break
    try:
        return l[-1] if len(l) >= 2 else None
    except:
        return None
