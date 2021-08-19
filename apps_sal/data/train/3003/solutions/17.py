def args_count(*args, **kwargs):
    counter = 0
    for arg in args:
        counter += 1
    if kwargs:
        for kwarg in kwargs:
            counter += 1
    return counter
