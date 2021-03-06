import re


def align_right(text, width):
    return '\n'.join((' ' * (width - len(line)) + line for (line, sep) in re.findall('(.{,' + str(width) + '})( |$)', text) if line))
