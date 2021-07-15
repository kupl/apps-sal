def args_count(*args, **kwargs):
    return len([x for x in args]) + len([y for y in kwargs.values()])
