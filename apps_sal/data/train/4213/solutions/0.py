def array_info(x):
    if not x:
        return 'Nothing in the array!'
    return [
        [len(x)],
        [sum(isinstance(i, int) for i in x) or None],
        [sum(isinstance(i, float) for i in x) or None],
        [sum(isinstance(i, str) and not i.isspace() for i in x) or None],
        [sum(isinstance(i, str) and i.isspace() for i in x) or None],
    ]
