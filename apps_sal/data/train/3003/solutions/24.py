# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    e = 0
    for i in args:
        e += 1
    for i in kwargs:
        e += 1
    return e
