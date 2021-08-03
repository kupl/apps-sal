import re


def make_sentences(parts):
    return re.sub(' ([,.])', r'\1', ' '.join(parts).replace(' ,', ',')).rstrip('.') + '.'
