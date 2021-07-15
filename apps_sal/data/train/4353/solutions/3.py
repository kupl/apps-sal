def could_be(original, another):
    o, a = set(original.split()), set(another.split())
    return a.issubset(o) if a and o else False
