from itertools import groupby

"""A RomanNumerals helper object"""


class RomanNumerals(object):
    letters = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
               ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

    @classmethod
    def to_roman(cls, val):
        rom = []
        for l, v in cls.letters:
            m = val // v
            rom += m * [l]
            val -= m * v
        return ''.join(rom)

    @classmethod
    def from_roman(cls, rom):
        cumu = 0
        for l, v in cls.letters:
            while rom[:len(l)] == l:
                rom = rom[len(l):]
                cumu += v
            if not rom:
                break
        return cumu
