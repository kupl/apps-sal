from string import ascii_uppercase

ALPHABET = str.maketrans(ascii_uppercase, "@ 8(D3F6


def to_leet_speak(text):
    return text.translate(ALPHABET)
