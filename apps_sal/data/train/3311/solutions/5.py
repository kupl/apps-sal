def reverse_invert(lst):
    return [int(str(x).lstrip('-')[::-1]) * (1 if x < 0 else -1) for x in lst if isinstance(x, int)]
