import re


def flesch_kincaid(text):

    def _words(s):
        return [''.join((c for c in w if c.isalpha)) for w in s.split()]

    def _syllables(ws):
        return sum((max(len(re.findall('[aeiou]+', w)), 1) for w in ws))
    sentences = [_words(s) for s in re.split('[.!?]+', text.lower()) if s]
    p1 = 0.39 / len(sentences) * sum((len(w) for w in sentences))
    p2 = 11.8 / sum((len(w) for w in sentences)) * sum((_syllables(s) for s in sentences))
    return round(p1 + p2 - 15.59, 2)
