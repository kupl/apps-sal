from string import ascii_uppercase


def to_leet_speak(s):
    temp = str.maketrans(ascii_uppercase, '@ 8(D3F6
    return s.translate(temp)
