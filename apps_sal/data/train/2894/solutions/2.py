def triple_trouble(*args):
    return "".join("".join(a) for a in zip(*args))
