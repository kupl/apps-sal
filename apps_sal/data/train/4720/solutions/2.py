def hp(arr):
    if not isinstance(arr, list):
        return ()
    elif not arr:
        return (0,)
    xs = list(map(hp, arr))
    if None not in xs and all((x == xs[0] for x in xs)):
        return (len(arr),) + xs[0]


hyperrectangularity_properties = hp
