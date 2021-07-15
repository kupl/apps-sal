def validate_code(code):
    import re
    return True if re.match('^1|^2|^3', str(code)) is not None else False
