def args_count(*args, **kwargs):
    ctr = 0
    for x in args:
        ctr += 1
    for y in kwargs:
        ctr += 1
    return ctr
