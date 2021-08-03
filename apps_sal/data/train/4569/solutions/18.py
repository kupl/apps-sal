def next_item(xs, item):

    xs = iter(xs)
    if item in xs:
        return next(xs, None)
 # TODO: Implement me
