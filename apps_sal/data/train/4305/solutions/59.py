def order_weight(strng):
    strng = ' '.join(sorted(strng.split()))
    return ' '.join(sorted(strng.split(), key=lambda x: sum(map(int, list(x)))))
