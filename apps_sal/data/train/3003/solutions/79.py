def args_count(*args, **kwargs):
    '''Return the number of passed arguments'''
    return len(args) + len(list(kwargs.keys()))

