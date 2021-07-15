def to_alternating_case(string):
    return "".join(list(i.lower() if i.isupper() else i.upper() for i in string))
