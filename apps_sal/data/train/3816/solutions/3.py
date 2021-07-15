def move_ten(s):
    return ''.join(chr(97 + (ord(x) - 97 + 10)%26) for x in s)
