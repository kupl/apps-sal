def args_count(*args, **kwargs):
    counter = 0
    for key in args:
        counter += 1
    for key in kwargs:
        counter += 1
    return counter
