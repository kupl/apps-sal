import re


def kontti(s):
    return re.sub('\\b([^aeiouy\\s]*[aeiouy])(\\S*)', 'ko\\2-\\1ntti', s, flags=re.I)
