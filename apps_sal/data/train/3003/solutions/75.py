def args_count(*a, **s):
    return a.__len__() + s.__len__()
