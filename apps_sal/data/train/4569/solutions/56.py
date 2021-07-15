def next_item(l, item):
    try:
        return l[l.index(item)+1] if item in l and l.index(item)+1 < len(l) else None
    except:
        return next(l)

