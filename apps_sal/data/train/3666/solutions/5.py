from re import compile, match
REGEX = compile('\\s*$')


def whitespace(string):
    return bool(match(REGEX, string))
