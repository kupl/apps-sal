import re
from functools import reduce


def is_matched(read):
    parse = re.findall(r'[0-9]+[A-Z]', read[0])
    cigar = {}
    for i in parse:
        if cigar.get(i[-1]) == None:
            cigar[i[-1]] = 0
        cigar[i[-1]] += int(i[:-1])
    if cigar.get('M') == len(read[1]):
        return True
    elif reduce(lambda x, y: x + y, [v for v in cigar.values()], 0) == len(read[1]):
        return False
    else:
        return 'Invalid cigar'
