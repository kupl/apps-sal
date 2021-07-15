def order_weight(strng):
    return ' '.join(sorted(strng.split(' '), 
        key=lambda s: (sum([int(a) for a in s]), s)))
