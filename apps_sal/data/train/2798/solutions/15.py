def to_alternating_case(string):
    return "".join([i.capitalize() if str.islower(i) else i.lower() for i in string])
