# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kvalues):
    s = len(args) + len(kvalues)
    return s
