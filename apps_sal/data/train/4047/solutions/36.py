import string


str1 = string.ascii_uppercase
str2 = '@8(D3F6#!JK1MN0PQR$7UVWXY2'

def to_leet_speak(s):
    table = str.maketrans(str1, str2)
    return s.translate(table)

