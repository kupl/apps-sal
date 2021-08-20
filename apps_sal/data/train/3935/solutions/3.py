import re


def vowel_recognition(s):
    return sum(((len(s) - m.start()) * (1 + m.start()) for m in re.finditer('(?i)[aeiou]', s)))
