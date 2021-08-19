# Create a function args_count, that returns count of passed arguments
def args_count(*args, **keys):
    return len(args) + len(keys)
