def args_count(*args, **kwargs):
    if not kwargs:
        return len(args)
    else:
        return len(args) + len(kwargs)
