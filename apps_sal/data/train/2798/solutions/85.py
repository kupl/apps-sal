def to_alternating_case(string):
    return ''.join(i.upper() if i == i.casefold() else i.casefold() for i in string)
