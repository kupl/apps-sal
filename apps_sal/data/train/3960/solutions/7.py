import textwrap


def align_right(text, width):
    wrapper = textwrap.TextWrapper(width=width, break_on_hyphens=True)
    return '\n'.join((line.rjust(width) for line in wrapper.wrap(text)))
