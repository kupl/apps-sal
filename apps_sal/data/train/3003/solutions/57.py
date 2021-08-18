def args_count(*args, **kwargs):
    counter = 0
    for item in args:
        counter += 1
    for key, value in list(kwargs.items()):
        counter += 1
    return counter
