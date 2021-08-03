import re


def interweave(s1, s2):
    return re.sub(r'\d', '', ''.join(a + b for a, b in zip(s1, s2.ljust(len(s1), ' ')))).strip()
