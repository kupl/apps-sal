def to_alternating_case(string):
    soln = ''

    for char in string:
        if char == char.lower():
            soln += char.upper()
        elif char == char.upper():
            soln += char.lower()
        elif char == '':
            soln += char
    return soln
