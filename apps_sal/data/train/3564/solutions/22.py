def stringy(size):

    if size % 2 == 0:
        return "10" * int(size / 2)
    else:
        x = size - 1
        return "10" * int(x / 2) + "1"
