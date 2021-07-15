from itertools import chain

def format_words(words):
    if not words: return ''
    
    filtered = [s for s in words if s]
    nCommas  = len(filtered)-2
    nAnd     = min(1,len(filtered)-1)
    chunks   = [', '] * nCommas + [' and '] * nAnd + ['']
    
    return ''.join(chain(*zip(filtered, chunks)))
