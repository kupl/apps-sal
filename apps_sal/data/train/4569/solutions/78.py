def next_item(xs, item):
    token=0
    for i in xs:
        if token==1: return i
        if i==item: token=1
    return None
