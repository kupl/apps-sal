def validate_code(code):
    import re
    return bool(re.match('^[123]\\d*$', str(code)))
