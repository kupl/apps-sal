def args_count(*args, **kwargs):
    try:
        return len(args) + len(kwargs)
    except TypeError:
        return 0
