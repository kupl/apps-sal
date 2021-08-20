def alternateCase(s):
    new_s = ''
    for char in s:
        if ord(char) > 122 or ord(char) < 65:
            new_s += char
            continue
        if ord(char) >= 97:
            new_s += chr(ord(char) - 32)
        else:
            new_s += chr(ord(char) + 32)
    return new_s
