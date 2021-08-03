from string import ascii_lowercase as aLow


def shifterAndSrc(c): return chr((ord(c) + SHIFT.get(c, DEFAULT) - 97) % 26 + 97), c


SHIFT = {'a': -5, 'e': -4, 'i': -5, 'o': -1, 'u': -5, 'c': -1, 'd': -3}
DEFAULT, REVERT = 9, 'code'
TABLE = str.maketrans(aLow, ''.join(c if c not in REVERT else o for c, o in map(shifterAndSrc, aLow)))


def vowel_back(s): return s.translate(TABLE)
