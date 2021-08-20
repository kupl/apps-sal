import re


def sort_poker(john, uncle):
    (j, s) = (re.findall('([SDHC])([0-9A-Z]0?)', john), ''.join(re.findall('[SDHC]', uncle)))
    n = '2 3 4 5 6 7 8 9 10 J Q K A'
    return ''.join(map(''.join, sorted(j, key=lambda c: (s.find(c[0]), n.find(c[1])))))
