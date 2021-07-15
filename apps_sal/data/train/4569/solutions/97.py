def next_item(xs, item):
    if type(xs) is str:
        xs = [x for x in xs]
    if type(xs) is list: # Convert list to generator, so that everything is generator
        xs = (x for x in xs)
    for x in xs: # Go over generator
        if x == item:
            try:
                return next(xs) # print(x)
            except StopIteration:
                return None
    return None
