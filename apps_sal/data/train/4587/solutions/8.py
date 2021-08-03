import re


def range_parser(string):
    return sum((list(range(int(m.group(1)), int(m.group(2) or int(m.group(1))) + 1, int(m.group(3) or 1))) for m in re.finditer(r'(\d+)(?:-(\d+)(?::(\d+))?)?', string)), [])
