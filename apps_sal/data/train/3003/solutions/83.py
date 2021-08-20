def args_count(*args, **kwargs):
    count = 0
    for arg in args:
        count += 1
    for (name, value) in list(kwargs.items()):
        count += 1
    return count
