import re


def toUnderScore(s):
    return re.sub('(?<=[^0-9])(\\d+)', '_\\1', re.sub('(?<=[^_])([A-Z])(?=[a-z]*)', '_\\1', s[0] + s[1:-1].replace('_', '') + s[-1])) if s else ''
