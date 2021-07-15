def next_item(xs, item): 
    it = iter(xs)
    try:
        while True:
            x = next(it)
            if x==item:
                x = next(it)
                return x
    except StopIteration:
        return None
