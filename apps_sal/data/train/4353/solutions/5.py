def could_be(original, another):
    (a, b) = (original.split(), another.split())
    return bool(a and b and (set(a) >= set(b)))
