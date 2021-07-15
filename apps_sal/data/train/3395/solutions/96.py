from collections import OrderedDict

def remove_duplicate_words(s):
    return ' '.join(OrderedDict((x,None) for x in s.split()).keys())
