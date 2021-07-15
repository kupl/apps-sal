def args_count(*args, **kwargs):
    print(*args)
    if len(kwargs.keys()) > 0:
        return len(args) + len(kwargs.keys())
    return len(args)
