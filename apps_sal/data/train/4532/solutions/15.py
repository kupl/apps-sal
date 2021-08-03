def validate_code(code):
    # your code here
    string = str(code)
    return True if string[0] in '123' else False
