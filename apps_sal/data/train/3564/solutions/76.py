def stringy(size):
    new = ""
    if size % 2 == 0:
        new += "10" * (size // 2)
    else:
        new += "10" * (size // 2)
        new += "1"
    return new
