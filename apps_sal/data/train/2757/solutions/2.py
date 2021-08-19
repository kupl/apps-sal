import re

PATTERN = re.compile(
    '^'                   # begin string
    '(?=.*?[A-Z])'        # at least one uppercase letter
    '(?=.*?[a-z])'        # at least one lowercase letter
    '(?=.*?\d)'           # at least one digit
    '(?=.*?[!@#$%^&*?])'  # at least one special character
    '[A-Za-z\d!@#$%^&*?]'  # only the given characters
    '{8,20}'              # between 8 and 20 characters long
    '$'                   # end string
)


def check_password(s):
    return "valid" if PATTERN.match(s) else "not valid"
