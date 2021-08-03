from collections import OrderedDict
def remove_duplicate_words(s): return ' '.join(OrderedDict.fromkeys(s.split(' ')))
