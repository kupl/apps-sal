ABC = 'abcdefghijklmnopqrstuvwxyz'


def change(s):
    s = set(s.lower())
    return ''.join((str(int(char in s)) for char in ABC))
