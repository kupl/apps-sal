from collections import Counter
from re import sub


def only_duplicates(s):
    return sub('[%s]' % ''.join((k for (k, v) in Counter(s).items() if v == 1)), '', s)
