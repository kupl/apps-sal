def args_count(*args, **kwargs):
    return len(args) + len(kwargs)
args_count(100, "tot", 3.5, 3, 2, 4, 2)
