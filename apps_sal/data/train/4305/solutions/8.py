def order_weight(strng):
    return ' '.join(sorted(strng.split(' '), key=lambda s: (sum([int(i) for i in s]), s)))
