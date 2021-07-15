def flatten(*args):
    return [a for arg in args for a in (flatten(*arg) if type(arg) is list else [arg])]
