def args_count(*args, **kwargs):
    new_list = []
    new_list.extend(tuple((*args, ))) if args else None
    new_list.extend(tuple((*kwargs, ))) if kwargs else None
    return len(new_list)
