def args_count(*args, **kwargs):
    return sum([1 for i in args]) + sum([1 for i in kwargs])
