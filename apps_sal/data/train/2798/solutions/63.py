def to_alternating_case(string):
    return ''.join(list(map(lambda s: s.lower() if s.isupper() else s.upper(), string)))
