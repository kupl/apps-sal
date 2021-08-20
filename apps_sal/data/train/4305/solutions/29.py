def order_weight(strng):

    def key(s):
        return (sum((int(d) for d in s)), s)
    return ' '.join(sorted(strng.split(), key=key))
