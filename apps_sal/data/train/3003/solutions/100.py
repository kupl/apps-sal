def args_count(*args, **kwargs):
    total = 0
    args = list(args) + list(kwargs)
    for i in args:
        total += 1
    return total
