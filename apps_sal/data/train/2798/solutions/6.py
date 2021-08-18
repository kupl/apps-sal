def to_alternating_case(string):
    return ''.join(string[i].upper() if string[i].islower() else string[i].lower() for i in range(len(string)))
