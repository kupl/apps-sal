import re


def dashatize(num):
    p = re.compile('([13579])')
    return p.sub('-\\1-', str(num)).replace('--', '-').strip('-')
