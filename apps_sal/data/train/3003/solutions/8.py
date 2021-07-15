# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kargs):
    return len(args) + len (kargs)
