def triple_trouble(*args):
    return "".join(map("".join, zip(*args)))
