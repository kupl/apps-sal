def array_mash(a, b):
    return [x for xs in zip(a, b) for x in xs]
