def to_alternating_case(string):
    empty_string = ''
    for i in string:
        if i.islower():
            empty_string = empty_string + i.upper()
        else:
            empty_string = empty_string + i.lower()
    return empty_string
