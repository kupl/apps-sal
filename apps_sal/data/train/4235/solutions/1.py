import re


def make_sentences(parts):
    return re.sub(' ([,.])', '\\1', ' '.join(parts).replace(' ,', ',')).rstrip('.') + '.'
