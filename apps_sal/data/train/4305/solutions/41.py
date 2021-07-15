def order_weight(strng):
    return " ".join(sorted(strng.split(" "), key=lambda s:(sum([int(c) for c in s]), s)))
