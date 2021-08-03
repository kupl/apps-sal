def decode(string):
    return string.translate(str.maketrans("1234567890", "9876043215"))
