def next_item(xs, item):
    iterXS = iter(xs)
    for i in iterXS:
        if i == item:
            try:
                return next(iterXS)
            except:
                return None
