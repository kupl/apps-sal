from copy import deepcopy


def combine(*args):
    if not args:
        return []
    args_list = list(deepcopy(args))
    first = args_list.pop(0)
    head = first.pop(0)
    if first:
        args_list.append(first)
    return [head] + combine(*tuple(args_list))
