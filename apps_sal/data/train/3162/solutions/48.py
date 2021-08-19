from re import search


def summation(string):
    if not string or search('[^a-zA-Z]', string):
        string = ''
    return sum((ord(x) for x in list(string.upper())))


def compare(s1, s2):
    return summation(s1) == summation(s2)
