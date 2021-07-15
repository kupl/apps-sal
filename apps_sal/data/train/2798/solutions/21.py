def to_alternating_case(string):
    return "".join(x.upper() if x.islower() else x.lower() for x in string)
