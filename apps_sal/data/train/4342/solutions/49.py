def no_space(x):
    new_string = ''
    for character in x:
        if character.isspace() == False:
            new_string += character
    return new_string
