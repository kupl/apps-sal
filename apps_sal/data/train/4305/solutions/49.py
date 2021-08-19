def order_weight(strng):
    # your code
    return ' '.join(sorted(sorted(strng.split()), key=lambda x: sum(int(a) for a in x), reverse=False))
