def args_count(*arg, **kwargs):
    print(arg, kwargs)
    return len(arg) + len(kwargs)
