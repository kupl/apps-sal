def uni_total(string):
    out = 0
    if not string:
        return 0
    for items in string:
        out += ord(items)
    return out
