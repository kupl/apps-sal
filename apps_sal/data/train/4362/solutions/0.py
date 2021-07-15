import re

def frogify(s):
    return ' '.join( ' '.join(re.findall(r'[a-z]+', sentence)[::-1]) + punct for sentence,punct in re.findall(r'(.*?)([.!?])', s) )
