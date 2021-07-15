def trim(a):
    return [["|" if y == "J" else y for y in x] for x in a[:-1]] + [["..."] * len(a[0])]
