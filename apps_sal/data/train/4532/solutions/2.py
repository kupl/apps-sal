def validate_code(code):
    import re
    return bool(re.match(r"^[123]\d*$",str(code)))

