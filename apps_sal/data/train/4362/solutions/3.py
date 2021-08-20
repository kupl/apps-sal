import re


def reverse_sentence(m):
    words = m.group(1).split()
    rev = ' '.join(reversed(words))
    return m.expand(' {}\\2'.format(rev))


def frogify(s):
    s = re.sub('[,;{}\\-\\(\\)]', '', s)
    return re.sub('(.*?)([.!?])', reverse_sentence, s).strip()
