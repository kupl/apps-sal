from string import ascii_uppercase

tr = str.maketrans(ascii_uppercase, '@ 8(D3F6


def to_leet_speak(s):
    return s.translate(tr)
