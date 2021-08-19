# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    return sum([1 for i in args] + [1 for i in kwargs])
