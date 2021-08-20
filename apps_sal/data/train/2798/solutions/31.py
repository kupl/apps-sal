def to_alternating_case(string):
    output = ''
    for character in string:
        if character.isupper():
            output += character.lower()
        else:
            output += character.upper()
    return output
