import re
PATTERN = re.compile('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\\d)(?=.*?[!@#$%^&*?])[A-Za-z\\d!@#$%^&*?]{8,20}$')


def check_password(s):
    return 'valid' if PATTERN.match(s) else 'not valid'
