from re import match as m

string_to_number = lambda s: eval(s) if m(r'^[-+]?\d+$', s) else None
