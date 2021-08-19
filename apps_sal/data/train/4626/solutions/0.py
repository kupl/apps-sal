def parse_character(char):
    if 65 <= ord(char) <= 90:
        return chr(155 - ord(char))
    elif 97 <= ord(char) <= 122:
        return chr(219 - ord(char))
    else:
        return char


def decode(string_):
    if not isinstance(string_, str):
        return 'Input is not a string'
    return ''.join(map(parse_character, string_))
