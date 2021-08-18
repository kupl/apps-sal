def args_count(*args, **kwargs):
    e = 0
    for i in args:
        e += 1
    for i in kwargs:
        e += 1
    return e
