def to_alternating_case(string):
    return "".join(list(map(lambda char: char.upper() if char.islower() else char.lower(), string)))
