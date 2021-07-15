def flatten_me(lst):
    from itertools import chain
    return list(chain.from_iterable([el] if not isinstance(el, list) else el for el in lst))
