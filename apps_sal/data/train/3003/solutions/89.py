def args_count(*args, **kwargs):
    arcount = 0
    for ar in args:
        arcount = 1 + arcount
    return (arcount + len(kwargs))
