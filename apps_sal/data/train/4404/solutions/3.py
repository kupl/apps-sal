import re
from distutils.version import LooseVersion

TRAILING_ZEROS = re.compile(r'(\.0+)+$')


def cmp(a, b):
    return (a > b) - (a < b)


def compare(s1, s2):
    return cmp(LooseVersion(TRAILING_ZEROS.sub('', s1)), LooseVersion(TRAILING_ZEROS.sub('', s2)))
