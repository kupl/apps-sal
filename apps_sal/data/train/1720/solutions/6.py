class RomanNumerals(object):
    
    @classmethod
    def to_roman(self, n, result='', i=0):
        SPQR = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
        (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        
        if i == len(SPQR):
            return result
        while n - SPQR[i][0] >= 0:
            result += SPQR[i][1]
            n -= SPQR[i][0]
        i += 1
        return self.to_roman(n, result, i)
        
        
    @classmethod
    def from_roman(self, roman, result=0, i=0):
        SPQR = ((900, 'CM'), (1000, 'M'), (400, 'CD'), (500, 'D'), (90, 'XC'), (100, 'C'), (50, 'L'),
        (40, 'XL'), (9, 'IX'), (10, 'X'), (4, 'IV'), (5, 'V'), (1, 'I'))
        
        if roman == '':
            return result
        while SPQR[i][1] in roman:
            result += SPQR[i][0]
            roman = roman[len(SPQR[i][1]):]
        i += 1
        return self.from_roman(roman, result, i)
