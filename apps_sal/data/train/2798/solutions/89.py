def to_alternating_case(string):
    result = []
    for letter in string:
        if letter.upper() == letter:
            result.append(letter.lower())
        elif letter.lower() == letter:
            result.append(letter.upper())

    return ''.join(result)
