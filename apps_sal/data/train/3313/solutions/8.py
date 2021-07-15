import re


def highlight(code):
    patterns = {
        'F': 'pink',
        'L': 'red',
        'R': 'green',
        '0-9': 'orange',
    }
    new_string = code
    for pattern, color in patterns.items():
        _pattern = re.compile(r'([{}]+)'.format(pattern))
        new_string = _pattern.sub(r'<span style="color: {}">\1</span>'.format(color), new_string)
    return new_string
