def args_count(*args, **kwargs):
    if len(kwargs.keys()) > 0:
        return len(args) + len(kwargs.keys())
    else:
        return len(args)
