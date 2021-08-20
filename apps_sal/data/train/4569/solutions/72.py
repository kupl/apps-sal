def next_item(xs, item):
    print('xs =', xs)
    xs = iter(xs)
    try:
        while next(xs) != item:
            pass
        return next(xs)
    except:
        return None
