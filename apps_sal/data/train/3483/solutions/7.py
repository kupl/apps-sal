def string_parse_gen(string):
    (counter, prev_char) = (0, '')
    for char in string:
        if char == prev_char:
            counter += 1
            if counter == 2:
                yield '['
        else:
            if counter >= 2:
                yield ']'
            prev_char = char
            counter = 0
        yield char
    if counter >= 2:
        yield ']'


def string_parse(string):
    return ''.join(list(string_parse_gen(string))) if isinstance(string, str) else 'Please enter a valid string'
