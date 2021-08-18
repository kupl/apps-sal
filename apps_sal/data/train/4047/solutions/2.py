table = str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '@ 8(D3F6
)


def to_leet_speak(text):
    return text.translate(table)
