def args_count(*args, **kwargs):
    s = 0
    for a in args:
        s += 1
    for key, value in list(kwargs.items()):
        s += 1
    return s
