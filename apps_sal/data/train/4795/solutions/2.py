import re


def flesch_kincaid(text):
    nLines = len(re.findall(r'([.?!;:]+)', text))
    nWords = text.count(' ') + 1
    nSyll = len(re.findall(r'([aeiou]+)', text, flags=re.IGNORECASE))
    return round(0.39 * nWords / nLines + 11.8 * nSyll / nWords - 15.59, 2)
