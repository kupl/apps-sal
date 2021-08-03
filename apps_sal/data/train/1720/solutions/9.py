class RomanNumerals:
    dic = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    @staticmethod
    def to_roman(n):
        res = []
        for i in RomanNumerals.dic:
            res.extend((n / i[0]) * i[1])
            n -= (n / i[0]) * i[0]

        return "".join(res)

    @staticmethod
    def from_roman(n):
        res = 0
        for i in RomanNumerals.dic:
            while n.startswith(i[1]):
                res += i[0]
                n = n[len(i[1]):]
        return res
