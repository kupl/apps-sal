def roman_fractions(num, fraction=0):
    rom = ''
    FACT = {1: '.', 2: ':', 3: ':.', 4: '::', 5: ':.:', 6: 'S', 7: 'S.', 8: 'S:', 9: 'S:.', 10: 'S::', 11: 'S:.:'}
    ENCO = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    EDGE = {0: lambda x, elem, dict, number: dict.get(elem, '') * number, 1: lambda e, i, D, l: e + D.get(i * (l + 1), 'M' * (l - 1)) if l in [4, 9] else D.get(i * l, 'M' * 5) if l is 5 else D[i * 5] + e * (l % 5)}
    if num < 0 or num > 5000 or (fraction and fraction not in FACT):
        return 'NaR'
    for element in list(ENCO.keys())[0::2][::-1]:
        left = num // element
        rom += EDGE.get(left > 3, '')(ENCO[element], element, ENCO, left)
        num %= element
    ret = rom + FACT.get(fraction, '')
    return ret if ret else 'N'
