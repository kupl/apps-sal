from re import compile
FIND = compile('((?:\\d{3})+?)(?:98)([01]+)(?:98)?').findall


def to_text(s):
    return ''.join((chr(int(s[i:i + 3]) - 4) for i in range(0, len(s), 3)))


def decode(number):
    return ', '.join((f'{to_text(x)}, {int(y, 2)}' for (x, y) in FIND(str(number))))
