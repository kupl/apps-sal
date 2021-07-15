def flatten(lst):
    return [x for xs in lst for x in (xs if isinstance(xs, list) else [xs])]
