def args_count(*args, **kwargs):
    a = 0
    for i in args:
        a += 1
    for i in kwargs:
        a += 1
    return a
