def to_leet_speak(str):
    str = str.upper()
    new = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","@8(D3F6#!JK1MN0PQR$7UVWXY2")
    return str.translate(new)

