def to_alternating_case(string):
    new_string = []
    for character in string:
        if character.isalpha():
            if character.islower():
                new_string.append(character.upper())
            elif character.isupper():
                new_string.append(character.lower())
        else:
            new_string.append(character)
    return ''.join(new_string)
