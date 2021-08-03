def args_count(*args, **kwargs):
    return len(args) + len(kwargs) if kwargs else len(args)
