from itertools import chain, zip_longest

# Credit to falsetru for the sentinel
sentinel = object()
def alternate_sort(l):
    positive = sorted(filter((0).__le__, l))
    negative = sorted(filter((0).__gt__, l), reverse=True)
    return list(filter(lambda x: x is not sentinel, chain.from_iterable(zip_longest(negative, positive, fillvalue=sentinel))))
