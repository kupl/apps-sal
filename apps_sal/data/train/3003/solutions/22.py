def args_count(*args, **kwargs):
    args_lst = [arg for arg in args]
    kwargs_lst = [kwarg for kwarg in kwargs]

    return len(args_lst) + len(kwargs_lst)
