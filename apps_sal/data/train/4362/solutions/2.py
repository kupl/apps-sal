import re


def rev(s):
    s, punc = s[:-1], s[-1]
    return ' '.join(word for word in s.split()[::-1]) + punc


def frogify(s):
    return ' '.join(rev(sentence).strip() for sentence in re.findall(r'.+?[.?!]', re.sub('[^ a-z.!?]', '', s)))
