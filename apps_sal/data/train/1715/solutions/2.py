import textwrap


def justify(text, width):

    def justify_line(line):
        if ' ' not in line:
            return line
        places = line.count(' ')
        spaces = width - len(line) + places
        (interval, extra) = divmod(spaces, places)
        return ''.join((word + ' ' * (interval + (i < extra)) for (i, word) in enumerate(line.split()))).strip()
    lines = textwrap.wrap(text, width, break_on_hyphens=False)
    return '\n'.join(list(map(justify_line, lines[:-1])) + [lines[-1]])
