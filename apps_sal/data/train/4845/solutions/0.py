def sort_nested_list(xsss):
    ys = iter(sorted((x for xss in xsss for xs in xss for x in xs)))
    return [[[next(ys) for x in xs] for xs in xss] for xss in xsss]
