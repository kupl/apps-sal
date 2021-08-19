def boolean_to_string(b):
    if isinstance(b, bool):
        return 'True' if b else 'False'
    return 'Wrong type'
