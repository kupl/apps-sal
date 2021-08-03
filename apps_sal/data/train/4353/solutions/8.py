def could_be(original, another):
    return bool(original and another and (set(original.split(' ')) >= set(another.split(' '))))
