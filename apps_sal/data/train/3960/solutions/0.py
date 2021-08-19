import textwrap


def align_right(text, width):
    return '\n'.join([l.rjust(width, ' ') for l in textwrap.wrap(text, width)])
