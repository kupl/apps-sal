import re

def filter_words(phrase):
    p = re.compile('(bad|mean|ugly|horrible|hideous)', re.IGNORECASE)
    return p.sub('awesome', phrase)
