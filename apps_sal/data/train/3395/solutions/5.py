from collections import OrderedDict
remove_duplicate_words=lambda s:' '.join(OrderedDict.fromkeys(s.split(' ')))

