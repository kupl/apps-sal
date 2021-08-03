def build_or_buy(hand):
    result = []

    b, w, g, s, o = [hand.count(st) for st in 'b,w,g,s,o'.split(',')]

    if b and w:
        result.append('road')
        if s and g:
            result.append('settlement')
    if o and g:
        if s:
            result.append('development')
        if o > 2 and g > 1:
            result.append('city')

    return result
