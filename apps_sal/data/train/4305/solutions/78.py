def order_weight(strng):
    weights = list()
    for x in strng.split():
        weights.append(sum([int(y) for y in x]))
    weight_counts = list(zip(strng.split(),weights))
    return ' '.join("{!s}".format(key) for key,value in sorted(weight_counts, key=lambda t: t[::-1]))
