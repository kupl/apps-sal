
class RomanNumerals():
    READ = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    INTG = {v: k for k, v in list(READ.items())}

    @classmethod
    def to_roman(cls, num, rom=''):
        EDGE = {
            0: lambda x, elem, dict, number: dict.get(elem, '') * number,
            1: lambda e, i, D, l: e + D[i * (l + 1)] if l in [4, 9] else D[i * l] if l is 5 else D[i * 5] + (e * (l % 5))
        }
        for element in list(cls.READ.keys())[0::2][::-1]:
            left = num // element
            rom += EDGE.get(left > 3, '')(cls.READ[element], element, cls.READ, left)
            num %= element
        return rom

    @classmethod
    def from_roman(cls, roma):
        cls.INTG.update({'N': 0})
        roma += 'N'
        return sum([-cls.INTG[x] if cls.INTG[x] < cls.INTG[z] else cls.INTG[x] for x, z in zip(roma[:-1], roma[1:])])
