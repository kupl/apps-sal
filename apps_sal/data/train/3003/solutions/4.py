def args_count(*args, **kwargs):
    args_counter = 0
    for _ in args:
        args_counter += 1
    for _ in kwargs:
        args_counter += 1
    return args_counter
