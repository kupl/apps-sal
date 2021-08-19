from string import ascii_lowercase as alc, digits


def mobile_keyboard(s):
    return sum(map(int, s.translate(str.maketrans('*#' + digits + alc, '1' * 12 + '234' * 6 + '5' + '234' * 2 + '5'))))
