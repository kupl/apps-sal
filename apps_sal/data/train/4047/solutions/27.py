def to_leet_speak(str):
    str = str.upper()
    new = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "@ 8(D3F6
    return str.translate(new)
