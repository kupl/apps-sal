def could_be(original, another):
    if not another.strip():
        return False
    return all((name in original.split() for name in another.split()))
