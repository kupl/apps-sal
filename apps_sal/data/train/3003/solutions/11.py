def args_count(*args, **kwargs):
    result = 0
    result = result + len(args) + len(kwargs)
    return result
