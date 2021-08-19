# Create a function args_count, that returns count of passed argument
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)
