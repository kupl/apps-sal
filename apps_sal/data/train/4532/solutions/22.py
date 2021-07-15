def validate_code(code):
    code = str(code)
    print(code)
    if str(code)[0] in ['1','2','3']:
        return True
    else:
        return False
