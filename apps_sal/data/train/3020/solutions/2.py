import re


def kontti(s):
    return re.sub('(\\S*?[aeiouy])(\\S*)', 'ko\\2-\\1ntti', s, flags=re.I)
