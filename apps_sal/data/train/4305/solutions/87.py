import operator


def order_weight(strng):
    modified = [(sum(map(int, x)), x) for x in strng.split()]
    return ' '.join(sort[1] for sort in sorted(modified, key=operator.itemgetter(0, 1)))
