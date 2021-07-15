def args_count(*args, **kwargs):
    total = [sum([+1 for arg in args]) + len(kwargs.keys()) if kwargs is not None else None]
    return total[0]
