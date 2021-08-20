def sort_key(s):
    return (sum((int(n) for n in list(s))), s)


def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=sort_key))
