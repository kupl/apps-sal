from re import match as m


def string_to_number(s): return eval(s) if m(r'^[-+]?\d+$', s) else None
