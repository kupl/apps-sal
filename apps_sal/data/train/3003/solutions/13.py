def args_count(*args, **kwargs):
    return len(args) if not kwargs else len(args)+len(kwargs)
