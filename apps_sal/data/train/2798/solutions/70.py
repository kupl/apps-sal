def to_alternating_case(string):
    return ''.join(map(lambda x: x.upper() if x.islower() else x.lower(), string))
