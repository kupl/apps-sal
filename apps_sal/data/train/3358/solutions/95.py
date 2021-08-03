
CORRECTIONS = {
    '0': 'O',
    '5': 'S',
    '1': 'I',
}

CORRECTION_TRANSLATION = str.maketrans(CORRECTIONS)


def correct(string):
    return string.translate(CORRECTION_TRANSLATION)
