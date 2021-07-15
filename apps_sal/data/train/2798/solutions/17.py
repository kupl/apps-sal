def to_alternating_case(string):
    return ''.join(map(lambda a : a.lower() if a.isupper() else a.upper(), string))
