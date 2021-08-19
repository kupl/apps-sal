def args_count(*args, **kwargs):
    return sum((len(x) for x in (args, kwargs)))
