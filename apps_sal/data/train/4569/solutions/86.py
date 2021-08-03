def next_item(xs, item):
    found = False
    result = None
    for x in xs:
        if found:
            result = x
            break
        if x == item:
            found = True
    return result
