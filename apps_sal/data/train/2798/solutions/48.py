def to_alternating_case(string):
    new_string = ''
    for i in string:
        new_string = new_string + i.lower() if i.isupper() else new_string + i.upper()
    return new_string
