def validate_code(code):
    import re
    return bool(re.match('[123]', str(code)))
