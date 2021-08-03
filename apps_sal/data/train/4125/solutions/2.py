import string as q


def get_weight(name):
    return sum(ord(char.swapcase()) for char in name if char in q.ascii_letters)
