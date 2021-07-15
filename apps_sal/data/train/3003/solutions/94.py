def args_count(*arg, **kwargs):
    count = 0
    for a in arg:
        count += 1
    return (count + len(kwargs.items()))
