def correct(string):
    errors = (('5', 'S'), ('0', 'O'), ('1', 'I'))
    for error in errors:
        string = string.replace(*error)
    return string
