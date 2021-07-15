def to_alternating_case(string):
    alternate = ''
    for char in string:
        if char == char.upper():
            alternate += char.lower()
        else:
            alternate += char.upper()
    return alternate
