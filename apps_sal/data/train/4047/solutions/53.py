from string import ascii_uppercase


def to_leet_speak(str):
    trans = str.maketrans(ascii_uppercase, '@ 8(D3F6
    return str.translate(trans)
