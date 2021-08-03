import re


def is_matched(cig):
    ci = re.split('\D', cig[0])[:-1]
    return 'Invalid cigar' if sum(map(int, ci)) != len(cig[1]) else cig[0] == ci[0] + 'M'
