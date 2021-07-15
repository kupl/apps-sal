def next_item(xs, item):
    xs = iter(xs)
    
    try:
        while True:
            elem = next(xs)
            if elem == item:
                break
    except StopIteration:
        return None
    

    try:
        return next(xs)
    except StopIteration:
        return None
