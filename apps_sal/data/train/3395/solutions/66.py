from collections import OrderedDict
from collections import Counter


def remove_duplicate_words(s):
    s = s.split(' ')
    s = OrderedDict.fromkeys(s)
    return ' '.join(s)
