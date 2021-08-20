REGEX = __import__('re').compile('MDZHB( \\d\\d){2}\\d [A-Z]+( \\d\\d){4}').fullmatch


def validate(message):
    return bool(REGEX(message))
