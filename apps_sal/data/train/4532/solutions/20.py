def validate_code(code):
    code = list(map(int, list(str(code))))
    return True if code[0] == 1 or code[0] == 2 or code[0] == 3 else False
