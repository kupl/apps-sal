from string import ascii_lowercase as alc, digits


def mobile_keyboard(s):
    return sum(map(int, s.translate(str.maketrans('*
