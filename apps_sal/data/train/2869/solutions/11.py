from collections import OrderedDict

def distinct(numbers):
    return list(OrderedDict.fromkeys(numbers).keys())
