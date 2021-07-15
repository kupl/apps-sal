import re
def sort_poker(H, U, OD='2 3 4 5 6 7 8 9 10 J Q K A'.split()):
    ORDER = re.findall(r'(.)\1*',re.sub(r'[\dJQKA]','', U))
    return ''.join(sorted(re.findall(r'[SDHC](?:[23456789JQKA]|10)',H), key=lambda x:(ORDER.index(x[0]), OD.index(x[1:]))))
