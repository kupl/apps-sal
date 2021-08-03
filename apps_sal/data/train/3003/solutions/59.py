def args_count(*args, **kwargs):
    index = 0
    for x in args:
        index = index + 1
    for x in kwargs:
        index = index + 1
    return index
