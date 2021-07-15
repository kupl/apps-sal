from textwrap import wrap

def align_right(text, width):
    return '\n'.join(line.rjust(width) for line in
                     wrap(text, width=width, break_on_hyphens=False))
