import re

def range_parser(string):
    result = []
    for match in re.finditer(r'(\d+)(?:-(\d+)(?::(\d+))?)?', string):
        start = int(match.group(1))
        end = int(match.group(2) or start) + 1
        step = int(match.group(3) or 1)
        result.extend(list(range(start, end, step)))
    return result
