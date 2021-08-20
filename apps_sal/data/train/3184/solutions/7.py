import re


def total_bill(s):
    return len(re.sub('r{5}', 'rrrr', re.sub('\\s+', '', s))) * 2
