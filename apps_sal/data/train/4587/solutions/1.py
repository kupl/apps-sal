import re


def range_parser(s):
    return [x for r in re.split(', *', s) for (start, end, step) in re.findall('(\\d+)-?(\\d*):?(\\d*)', r) for x in range(int(start), int(end or start) + 1, int(step or '1'))]
