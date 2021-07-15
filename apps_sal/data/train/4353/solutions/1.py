def could_be(original, another):
    original, another = (set(s.split()) for s in (original, another))
    return bool(another) and another <= original
