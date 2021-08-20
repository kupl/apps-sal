def calc(x):
    return ''.join((str(ord(ch)) for ch in x)).count('7') * 6
