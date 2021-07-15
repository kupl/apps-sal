def stringy(size):
    string = ""
    if size % 2 == 0:
        return "10" * (int(size / 2))
    else:
        return str("10" * int(size / 2 + 1))[:-1]
