def calc(string):
    return "".join(str(ord(char)) for char in string).count("7") * 6
