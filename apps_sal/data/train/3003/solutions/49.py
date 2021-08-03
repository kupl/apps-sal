# Create a function args_count, that returns count of passed arguments
def args_count(*n, **s):
    return len(n) + len(s)
