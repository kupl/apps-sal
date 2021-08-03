from collections import OrderedDict


def remove_duplicate_words(s):
    spliter = s.split()
    return " ".join(OrderedDict.fromkeys(spliter))
