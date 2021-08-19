from functools import cmp_to_key


def sum_digits(num):
    return sum([int(d) for d in str(num)])


def sort_weights(w1, w2):
    w1_total = sum_digits(w1)
    w2_total = sum_digits(w2)
    if w1_total == w2_total:
        if str(w1) < str(w2):
            return -1
        return 1
    else:
        return w1_total - w2_total


def order_weight(strng):
    if not strng:
        return ''
    weights = [int(x) for x in strng.split(' ')]
    sorted_weights = sorted(weights, key=cmp_to_key(sort_weights))
    return ' '.join(map(str, sorted_weights))
