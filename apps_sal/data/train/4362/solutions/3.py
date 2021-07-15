import re

def reverse_sentence(m):
    words = m.group(1).split()
    rev = ' '.join(reversed(words))
    return m.expand(r' {}\2'.format(rev))

def frogify(s):
    s = re.sub(r'[,;{}\-\(\)]', '', s)
    return re.sub(r'(.*?)([.!?])', reverse_sentence, s).strip()
