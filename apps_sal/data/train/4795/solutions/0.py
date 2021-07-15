from re import compile as reCompile

SENTENCE = reCompile(r'[.!?]')
SYLLABLE = reCompile(r'(?i)[aeiou]+')

def count(string, pattern):
    return len(pattern.findall(string))

def flesch_kincaid(text):
    nWords = text.count(' ') + 1
    return round(0.39 * nWords / count(text, SENTENCE) + 11.8 * count(text, SYLLABLE) / nWords - 15.59, 2)
