def validate_code(code):
    code_str = str(code)
    if code_str[0] == '1' or code_str[0] == '2' or code_str[0] == '3':
        return True
    return False
