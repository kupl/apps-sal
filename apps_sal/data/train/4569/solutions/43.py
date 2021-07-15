def next_item(xs, item):
    xs = iter(xs)
    for element in xs:
        if element == item:
            try:
                return next(xs)
            except:
                pass
        


