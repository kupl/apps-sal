def parse_float(string):
    return None if len([c for c in string if c not in '.0123456789']) else float(string)
