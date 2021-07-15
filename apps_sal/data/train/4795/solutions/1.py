import re

def flesch_kincaid(text):
    
    _words = lambda s: [''.join(c for c in w if c.isalpha) for w in s.split()]
    
    _syllables = lambda ws: sum(max(len(re.findall('[aeiou]+', w)), 1) for w in ws)
    
    sentences = [_words(s) for s in re.split(r'[.!?]+', text.lower()) if s]
    p1 = 0.39 / len(sentences) * sum(len(w) for w in sentences) 
    p2 = 11.8 / sum(len(w) for w in sentences) * sum(_syllables(s) for s in sentences) 
    return round(p1 + p2 - 15.59, 2)

