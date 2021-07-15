import re

def range_parser(string):
    return sum((list(range(int(start), int(end or start) + 1, int(step or 1)))
        for start, end, step in re.findall(r"(\d+)(?:-(\d+)(?::(\d+))?)?", string)), [])
