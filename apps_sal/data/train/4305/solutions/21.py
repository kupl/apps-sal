def order_weight(string):
    s = sorted([(sum([int(n) for n in num.strip()]), num.strip()) for num in string.split(' ')])
    return ' '.join(map(lambda t: t[1], s))
