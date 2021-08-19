def convert(s):
    return ''.join((chr(int(s[i:i + 2])) for i in range(0, len(s), 2)))
