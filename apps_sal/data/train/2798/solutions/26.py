def to_alternating_case(string):
    alter_case = lambda let: let.lower() if let.isupper() else let.upper()
    return ''.join(map(alter_case, string))
