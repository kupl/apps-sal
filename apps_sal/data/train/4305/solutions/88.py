def order_weight(strng):
    strng = sorted(strng.split())
    result = sorted(strng, key=lambda elem: sum([int(x) for x in elem]))
    return ' '.join(result)
