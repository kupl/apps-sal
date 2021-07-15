def to_alternating_case(s):
    return str().join([i.lower() if i.isupper() else i.upper() for i in s])
