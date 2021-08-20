def to_lover_case(stg):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', f"{'LOVE' * 6}LO")
    return stg.lower().translate(table)
