def array_info(x):
    if not x:
        return 'Nothing in the array!'
    ints = floats = strings = whitespaces = 0
    for e in x:
        if isinstance(e, str):
            if e.isspace():
                whitespaces += 1
            else:
                strings += 1
        else:
            if float(e).is_integer():
                ints += 1
            else:
                floats += 1
    return [[c or None] for c in (len(x), ints, floats, strings, whitespaces)]
