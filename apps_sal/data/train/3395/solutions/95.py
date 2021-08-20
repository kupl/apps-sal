from collections import OrderedDict


def remove_duplicate_words(s):
    a = s.split(' ')
    return ' '.join(list(OrderedDict.fromkeys(a)))
