from collections import Counter, OrderedDict


def odd_one_out(s):
    return list(reversed([item[0] for item in OrderedDict(Counter(s[::-1])).items() if int(item[1]) % 2 == 1]))
