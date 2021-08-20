def to_alternating_case(string):
    letters = [i for i in string]
    for i in range(len(letters)):
        if letters[i].islower():
            letters[i] = letters[i].upper()
        else:
            letters[i] = letters[i].lower()
    return ''.join(letters)
