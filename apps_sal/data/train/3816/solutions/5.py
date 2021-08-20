def move_ten(s):
    return ''.join((chr((ord(e) - 87) % 26 + 97) for e in s))
