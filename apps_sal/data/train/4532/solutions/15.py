def validate_code(code):
    string = str(code)
    return True if string[0] in '123' else False
