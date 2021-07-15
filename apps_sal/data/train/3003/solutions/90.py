# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    if not kwargs:
        return len(args)
    else:
        return len(args) + len(kwargs)
