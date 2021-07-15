def next_item(xs, item):
    """return first item in xs after item"""
    found = False
    for c in xs:
        if found: return c
        if c == item:
            found = True
    return None 
