def to_lover_case(string):
    return "".join("LOVE"[(ord(c) - 97) % 4] if c.isalpha() else c for c in string)
