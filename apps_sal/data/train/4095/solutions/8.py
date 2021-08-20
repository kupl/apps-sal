def added_char(s1, s2):
    return chr(int((sum((ord(x) for x in s2)) - sum((ord(x) for x in s1))) / 3))
