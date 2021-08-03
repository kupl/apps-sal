def no_space(x):
    new_string = ""
    for letter in x:
        if letter == " ":
            continue
        else:
            new_string += letter
    return new_string
