def validate_code(code):
    return True if str(code)[0] in set('123') else False
