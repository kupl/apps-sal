def order_weight(strng):
    # your code
    return " ".join(sorted(strng.split(), key=lambda x: (sum(map(int, x)), str(x))))
