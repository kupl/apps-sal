ROMANS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
s_numbers = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
ROMANS.update(s_numbers)
ROMANS = {v:k for k, v in ROMANS.items()}

lst = ['', '.', ':', ':.', '::', ':.:', 'S', 'S.', 'S:', 'S:.', 'S::', 'S:.:']


def roman_fractions(integer, fraction=None):
    if integer == 0 and fraction in [None, 0]:
        return 'N'
    if integer < 0 or integer > 5000 or (integer == 0 and (fraction >= 12 or fraction < 0)):
        return "NaR"
    if fraction != None:
        if fraction < 0 or fraction >= 12:
            return "NaR"
    roman = ''
    for a in reversed(sorted(ROMANS.keys())):
        while (a <= integer):
            integer = integer - a;
            roman = roman + ROMANS[a]
    return roman + lst[fraction] if fraction != None else roman
