def to_alternating_case(string):
    new = []
    for letter in string:
        if letter.isupper():
            new.append(letter.lower())
        elif letter.islower():
            new.append(letter.upper())
        else:
            new.append(letter)
    return ''.join(new)
