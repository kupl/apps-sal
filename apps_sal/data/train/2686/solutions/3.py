from string import ascii_lowercase
trans = str.maketrans(ascii_lowercase, "bcdEfghIjklmnOpqrstUvwxyzA")


def changer(string):
    return string.lower().translate(trans)
