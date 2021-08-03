def to_alternating_case(string):
    new_s = ""
    for char in string:
        if char.isupper():
            new_s += char.lower()
        else:
            new_s += char.upper()

    return new_s
