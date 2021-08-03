def correct(string):
    for letter in (("5", "S"), ("0", "O"), ("1", "I")):
        string = string.replace(*letter)
    return string
