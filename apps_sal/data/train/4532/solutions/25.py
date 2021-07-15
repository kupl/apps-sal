def validate_code(code):
    import re
    
    if re.match(r'^[1-3]', str(code)) is not None:
        return True
    else:
        return False
