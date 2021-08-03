import re


def validate_code(code):
    return bool(re.match("[123]{1}.*", str(code)))
