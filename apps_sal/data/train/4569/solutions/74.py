def next_item(xs, item):
    y = False
    for x in xs:
        if y:
            return x
        if item == x:
            y = True   
