def args_count(*args, **kwargs):
    if kwargs is not None:
        return len(args) + len(kwargs)
    return len(args)
