def getSum(n):
    return sum([int(x) for x in n])


def order_weight(s):
    return ' '.join(sorted(s.split(), key=lambda x: [getSum(x), x]))
